#                Data Wrangling, Transformation, and Management
#  What it is: Data wrangling involves cleaning and organizing raw data into a more usable format. 
#  Transformation includes changing data types, creating new features, handling missing values, etc.


import pandas as pd
import numpy as np
import io
from io import StringIO


df = pd.DataFrame(np.array([[1, 6, 2],[2, np.nan, 1],[np.nan, np.nan, 9]]))
df.columns = ['Q', 'Z', 'H']

# drop or fill NaN values in a dataframe

# Fill up all values with an R
df.fillna('R')

#drop all rows with NaN values
df.dropna()

# backfill and frontfill data point
df.bfill().ffill()

# drop multiple columns 
df.drop(['Salary', 'Name'], axis=1, inplace=True)


#Data Merging and Aggregation
#What it is: Combining data from multiple sources or tables and aggregating it for analysis (e.g., summing sales per region).
#Key Skills:
#JOIN operations in SQL (e.g., INNER JOIN, LEFT JOIN, RIGHT JOIN).
#Aggregating data using group-by functions (e.g., GROUP BY, COUNT(), SUM(), AVG()).
#Pandas methods such as merge(), concat(), and groupby().



data = """Name,Age,Gender,Salary
John,25,Male,50000
Alice,30,Female,55000
Bob,22,Male,40000
Eve,35,Female,70000
Charlie,28,Male,48000"""

df = pd.read_csv(io.StringIO(data))

# Create a new DataFrame to be combined with the original one
new_data = pd.DataFrame({
    'Name': ['Grace', 'Sophia'],
    'Age': [40, 27],
    'Gender': ['Female', 'Female'],
    'Salary': [65000, 52000]
})

# Combine the original DataFrame with the new data. Creates a new df
combined_df = pd.concat([df, new_data], ignore_index=True)

# Append the new data to the original DataFrame. COmbined it in the same dataframe
df = df.append(new_data, ignore_index=True)

# Merge the two DataFrames based on the 'Name' column. Like a join statement in SQL.
df2 = pd.DataFrame({
    'Name': ['John', 'Alice', 'Bob'],
    'Department': ['HR', 'IT', 'Finance']
})

merged_df = pd.merge(df, df2, on='Name', how='inner')

# Group By and aggregated data of Name and Gender: https://www.geeksforgeeks.org/python-pandas-dataframe-groupby/

aggregated_data = df.groupby(['Name', 'Gender']).agg(
    total_salary=('Salary', 'sum'),
    avg_salary=('Salary', 'mean'),
    player_count=('Name', 'count')
)

# Rank each Person based on their Gender and salary

df['Rank'] = df.groupby('Gender')['Salary'].transform(lambda x: x.rank(ascending=False))

# Filter groups using Salary > 45K

filtered_df = df.groupby('Gender').filter(lambda x: x['Salary'].mean() >= 45000)
print(filtered_df)
