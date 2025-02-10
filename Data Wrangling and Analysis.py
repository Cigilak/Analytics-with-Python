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

# Assume that you have a date column with dates for a month. First element of a date grouping is filled and next 3 are empty with a string
           date 
0    2022-07-01
1          -  
2          -
3          -
4    2022-07-02
#How will you clean this and ffill ? >> First convert the column into a date format >> Replace the string >> Front fill out the date column with ffill.
df['date'] = pd.to_datetime(df['date'])
df['date'] = df['date'].str.replace('-', '')
df['date'].fillna(method='ffill', inplace=True)

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

# Get the unique values of 'Salary' column
unique_values = df['Salary'].unique()

# Clean your datatype in a dataframe
def clean_data_types(df):
    for col in df.columns:
        if df[col].dtype == 'int64':
            df[col] = df[col].astype('int32')
        elif df[col].dtype == 'float64':
            df[col] = df[col].astype('float32')
        elif df[col].dtype == 'object':
            # Replace NaN values with "null" for object type columns
            df[col] = df[col].fillna("null")
    return df

#get null values from a dataframe

df[pd.isnull(df['DATE'])]


# Aggregate Data and group it a function to calculate and map based on the function

# Calculate weighted indicators based on Department
def get_cost(type):
    if type == 'IT': 
        return 4000 
    elif type == 'HR': 
        return 5000 
    else: 
        return 6000 
# Calculate weighted indicator cost. 
df['COST'] = df['TYPE'].map(get_cost)

# Get median cost of each department per row in a dataframe and divide it by 2 
avg_route_fares = (
                        roundtrip_tickets.groupby('DEPARTMENT')['COST']
                        .median()
                        .div(2) # roundtrip/2
                        .reset_index(name='MEDIAN_COST')
                    )
#Identify Null values in a dataframe column Salary
df[pd.isnull(df['Salary'] )]
