#                Data Wrangling, Transformation, and Management
#  What it is: Data wrangling involves cleaning and organizing raw data into a more usable format. 
#  Transformation includes changing data types, creating new features, handling missing values, etc.


import pandas as pd
import numpy as np

df = pd.DataFrame(np.array([[1, 6, 2],[2, np.nan, 1],[np.nan, np.nan, 9]]))
df.columns = ['Q', 'Z', 'H']
df
# drop or fill NaN values in a dataframe

# Fill up all values with an R
df.fillna('R')

#drop all rows with NaN values
df.dropna()

# backfill and frontfill data point
df.bfill().ffill()
