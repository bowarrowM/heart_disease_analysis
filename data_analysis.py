import pandas as pd

from all_imports import *

# EDA - Exploratory Data Analysis

# Display the first few rows of the dataframe
print(f"Display the first few rows of dataframe \n {df.head()}\n")

# Get basic information about the dataframe
print(f"Basic information about the dataframe \n {df.info()}\n")

# Summary statistics
print(f"Summary statistics of the df \n {df.describe}\n")

# View columns
print(f"View columns \n {df.columns}\n")

# Check for missing values
print(f"Check for missing(null) values \n {df.isnull().sum()}\n")

# Check for duplicates
print(f"Check for duplicates \n {df.duplicated().sum()}\n")

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------