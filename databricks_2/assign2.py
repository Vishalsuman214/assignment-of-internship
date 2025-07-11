dbutils.widgets.text("ProcessName","")
input_process=dbutils.widgets.get("ProcessName")

filtered_df = df.filter(df["ProcessName"] == input_process)
filtered_df.display()

tables={}
logics={}


for row in filtered_df.collect():
   tname=row["RawTableName"]
   col_name=row["RawTableCol"]
   datatype=row["RawTableDatatype"]
   logic=row["Logic"]
   

   if tname not in tables:
     logics[tname] = {}
     tables[tname]=[]
   logics[tname][col_name] = logic
   tables[tname].append((col_name,datatype))

layers=["raw","curated"] 

for l in layers:
   spark.sql(f"CREATE DATABASE IF NOT EXISTS {l}")
   for table_name,columns in tables.items():
     schema_str = ", ".join([f"{col} {dtype.upper()}" for col, dtype in columns])
     spark.sql(f"CREATE OR REPLACE TABLE {l}.{table_name} ({schema_str}) USING DELTA")
  
     print(f" Created table {l}.{table_name} with schema: {schema_str}")

spark.sql("""
INSERT INTO raw.user (id, name)
  VALUES 
    ('201', 'David'),
    ('202', 'Emma'),
    (NULL,'QASD')
""") 

spark.sql("""
select * from raw.user
""").display()

for table_name in logics:
    logic_exprs = []

    for col, logic in logics[table_name].items():
        if logic and logic.strip().lower() != "none":
            logic_exprs.append(f"{logic} AS {col}")
        else:
            logic_exprs.append(col)

    select_expr = ", ".join(logic_exprs)
    spark.sql(f"""
        INSERT OVERWRITE TABLE curated.{table_name}
        SELECT {select_expr}
        FROM raw.{table_name}
        WHERE {logics[table_name]['Id']}
    """)

    print(f" Inserted rows with non-null ID into curated.{table_name}")


spark.sql("""
select * from curated.user
""").display()