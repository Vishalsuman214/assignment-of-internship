import pandas as pd


df=pd.read_csv('lead.csv')


print("first 5 rows\n",df.head())
print("discriptions of columns\n",df.describe())

print("number of rows and columns\n",df.shape)

print("column names\n",df.columns)

print("data types of columns\n",df.dtypes)

print("missing values\n",df.isnull().sum())

print("unique values in each column\n",df.nunique())

print("sum of all values in each column\n",df.sum())



print("maximum value in each column\n",df.max())

print("minimum value in each column\n",df.min())

print(df['Index'])

filtered_df = df[df['Index'] >= 1000]

print(filtered_df)

group_data=df.groupby('Company')['Index'].mean()

print(group_data)

