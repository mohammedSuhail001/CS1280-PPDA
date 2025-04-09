import pandas as pd

# Loading a CSV file into a DataFrame
df = pd.read_csv(r"C:SHANTI\RVU\Programs\Minors\IDA\Activities\Datasets\6Mednull_values.csv")
print("Original DataFrame:")
print(df)

# Identifying missing values
print("\nMissing values in the DataFrame:")
print(df.isnull().sum())

# Filling missing values with appropriate methods
df.fillna(df.mean(numeric_only=True), inplace=True)  # Fill numeric columns with mean
df.fillna(method='ffill', inplace=True)  # Forward fill for categorical columns
print("\nDataFrame after filling all missing values:")
print(df)

# Dropping duplicate rows
df.drop_duplicates(inplace=True)
print("\nDataFrame after dropping duplicates:")
print(df)
