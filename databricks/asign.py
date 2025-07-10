df = spark.table("workspace.default.meta_data")
display(df)

def create_tables_from_metadata(metadata_df, layer):
    col_map = {
        "Raw": {"table_name": "RawTableName", "column_name": "RawTableColumn", "datatype": "RawTableColDatatype"},
        "Curated": {"table_name": "CuratedTableName", "column_name": "CuratedTableColumn", "datatype": "CuratedTableColumnDatatype"},
        "Presentation": {"table_name": "PresntationLayTableName", "column_name": "PresentationLayercolumn", "datatype": "PresentationLayerColDatatype"}
    }
    cols = col_map[layer]
    tables = metadata_df.select(cols["table_name"]).distinct().collect()
    
    for table in tables:
        table_name = table[cols["table_name"]]
        if table_name and table_name.strip():
            columns = metadata_df.filter(metadata_df[cols["table_name"]] == table_name) \
                                 .select(cols["column_name"], cols["datatype"]).distinct()
            create_stmt = f"CREATE TABLE {table_name} (\n" + ",\n".join([
                f"  {row[cols['column_name']]} {row[cols['datatype']]}" 
                for row in columns.collect() if row[cols['datatype']] != "NULL"
            ]) + "\n)"
            spark.sql(f"DROP TABLE IF EXISTS {table_name}")
            spark.sql(create_stmt)
            print(f"Created {layer} table: {table_name}")

print("Starting table creation process...")
create_tables_from_metadata(df, "Raw")
create_tables_from_metadata(df, "Curated")
create_tables_from_metadata(df, "Presentation")
print("Table creation completed!")

print("\nList of created tables:")
display(spark.sql("SHOW TABLES"))