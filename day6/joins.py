import pandas as pd


df1 = pd.DataFrame({
    'ID': [1, 2, 3, 4],
    'Name': ['A', 'B', 'C', 'D'],
    'Age': [25, 30, 35, 40]
})


df2 = pd.DataFrame({
    'ID': [3, 4, 5, 6],
    'Name': ['C', 'D', 'E', 'F'],
    'Age': [35, 40, 45, 50] 
})

# Inner join 
print("Inner Join:\n")
print(pd.merge(df1, df2, on='ID', how='inner'))

# Left join 
print("\nLeft Join:\n")
print(pd.merge(df1, df2, on='ID', how='left'))

# in this left or right side shows by Df1 and df2, the missing values are filled with NaN
# all the values of left side will be displayed
# but in right side, the missing values will be filled with NaN

# Right join 
print("\nRight Join:\n")
print(pd.merge(df1, df2, on='ID', how='right'))



# Merge multiple DataFrames on multiple columns 
print("\nMerge on ID and Name:\n")
print(pd.merge(df1, df2, on=['ID', 'Name'], how='inner', suffixes=('_df1', '_df2')))
