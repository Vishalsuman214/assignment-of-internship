import pandas as pd
import os

csv_path = 'lead.csv'

if not os.path.exists(csv_path):
    print(f"Error: File '{csv_path}' not found.")
else:
    df = pd.read_csv(csv_path)

    print("First 5 rows:\n", df.head())
    print("\nDescription of columns:\n", df.describe())
    print("\nNumber of rows and columns:", df.shape)
    print("\nColumn names:", df.columns.tolist())
    print("\nData types:\n", df.dtypes)
    print("\nMissing values:\n", df.isnull().sum())
    print("\nUnique values per column:\n", df.nunique())
    print("\nSum of all values (numeric columns):\n", df.select_dtypes(include='number').sum())
    print("\nMaximum value in each column:\n", df.select_dtypes(include='number').max())
    print("\nMinimum value in each column:\n", df.select_dtypes(include='number').min())

    if 'Index' in df.columns:
        print("\nColumn 'Index':\n", df['Index'])
        filtered_df = df[df['Index'] >= 10]
        print("\nFiltered rows (Index >= 1000):\n", filtered_df)
    else:
        print("\nColumn 'Index' not found in data.")

    if 'Company' in df.columns and 'Index' in df.columns:
        group_data = df.groupby('Company')['Index'].mean()
        print("\nAverage Index by Company:\n", group_data)
    else:
        print("\nCannot group by 'Company' or 'Index' column missing.")