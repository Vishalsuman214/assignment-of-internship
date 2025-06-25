import pandas as pd


df1 = pd.DataFrame({
    'ID': [1, 2, 3],
    'Name': ['A', 'B', 'C']
})

df2 = pd.DataFrame({
    'ID': [2, 3, 4],
    'Age': [30, 35, 40]
})


df1 = df1.set_index('ID')
df2 = df2.set_index('ID')


result = df1.join(df2, how='inner')

print(result)
