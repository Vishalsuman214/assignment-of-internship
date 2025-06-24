import pandas as pd

#diffrent way to iterate over rows in pandas dataframe
df = pd.DataFrame({
    'Name': ['rahul', 'sandeep', 'sanchit'],
    'Age': [25, 30, 28],
    'City': ['jaipur', 'delhi', 'mumbai']
})

for i ,row in df.iterrows():
    print(row['Name'], row['Age'])
    
# Selecting rows based on a condition
print(df[df['Age'] > 25])

# select any row using iloc[]
print(df.iloc[1]) 
print(df['Name'][:3])

#drop rows based on condition
df1=df[df['Age'] > 25]
print(df1)

# insert row at given position 
r=pd.DataFrame([['pawan', 20, 'delhi']], columns=['Name', 'Age', 'City'])
df2=pd.concat([df, r], ignore_index=True)
print(df2)

# list from rows
r_list=df.to_dict('records')
print(r_list)
