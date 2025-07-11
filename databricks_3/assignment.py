df=spark.table("data")
display(df)

dbutils.widgets.text("input"," ")
process_name=dbutils.widgets.get("input")
df=df.filter(df.ProcessName==process_name)
display(df)

raw_df={}

for row in df.collect():
  raw_table=row['RawTableName']
  raw_table_col=f"{row['RawTableCol']} {row['RawTableColDataType']}"

  if raw_table in raw_df:
      raw_df[raw_table].append(raw_table_col)
  else:
      raw_df[raw_table]=[raw_table_col]

display(raw_df)