# Databricks notebook source
SPARK_VERSION=3.2

# COMMAND ----------

import os
os.environ["SPARK_VERSION"]="3.3"

# COMMAND ----------

dbutils.widgets.text("arrival_date","2024-07-25")
date_str=dbutils.widgets.get("arrival_date")

# COMMAND ----------

customer_data=f"dbfs:/Volumes/workspace/travel/customer/customers_{date_str}.csv"

# COMMAND ----------

customer_df = spark.read \
    .format("csv") \
    .option("header", "true") \
    .option("inferSchema", "true") \
    .option("quote", "\"") \
    .option("multiline", "true") \
    .load(customer_data)
customer_df.printSchema()

# COMMAND ----------

display(customer_df)

# COMMAND ----------

from pyspark.sql.functions import col
def isComplete(self,column):
        null_count = self.filter(col(column).isNotNull())
        return null_count 
    

# COMMAND ----------

customer_df=isComplete(customer_df,"customer_id") 


# COMMAND ----------

display(customer_df)

# COMMAND ----------

from pyspark.sql.functions import current_date, lit

customer_df = (
    customer_df
    .withColumn("start_date",current_date())
    .withColumn("end_date", lit("2200-01-01").cast("date"))
    .withColumn("current_flag", lit("Y"))
)
display(customer_df)

# COMMAND ----------

# save the df_select data as a delta table inside default schema with schema evolution enabled
customer_df.write.format("delta").mode("overwrite").option("mergeSchema", "true").saveAsTable("default.travel_customer")

# COMMAND ----------

travel_customer_df = spark.table("default.travel_customer")


# COMMAND ----------

combined_df = travel_customer_df.unionByName(customer_df)


# COMMAND ----------

display(combined_df)

# COMMAND ----------

from pyspark.sql.functions import col, current_date, date_sub, lit

#  New updated or new customers (start_date = today and flag = 'Y')
new_updated_records_df = combined_df.filter(
    (col("start_date") == current_date()) & (col("current_flag") == "Y")
)
display(new_updated_records_df)





# COMMAND ----------

#  Old versions of updated customers (same IDs as new ones and current_flag = 'Y')
old_records_to_update = travel_customer_df.alias("old").join(
    new_updated_records_df.select("customer_id").alias("new"),
    on="customer_id"
).filter(col("old.current_flag") == "Y")

updated_old_records_df = old_records_to_update.withColumn(
    "end_date", date_sub(current_date(), 1)
).withColumn(
    "current_flag", lit("N")
)

# COMMAND ----------

display(updated_old_records_df)

# COMMAND ----------

#  Unchanged old records (those not being updated)
unchanged_old_records_df = travel_customer_df.join(
    old_records_to_update.select("customer_id"), on="customer_id", how="left_anti"
)

# COMMAND ----------

display(unchanged_old_records_df)

# COMMAND ----------


#  Truly new customers (not even present in old table)
new_customers_df = new_updated_records_df.join(
    travel_customer_df.select("customer_id"), on="customer_id", how="left_anti"
)

# COMMAND ----------

display(new_customers_df)

# COMMAND ----------


# Final combined DataFrame
final_customer_df = unchanged_old_records_df.unionByName(updated_old_records_df).unionByName(new_updated_records_df)


# COMMAND ----------

display(final_customer_df)

# COMMAND ----------
# overwrite the delta table with final_customer_df
final_customer_df.write.format("delta").mode("overwrite").saveAsTable("default.travel_customer")


# COMMAND ----------

display(spark.sql("select * from default.travel_customer"))