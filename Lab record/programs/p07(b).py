import pandas as pd

# Loading a CSV file into a DataFrame
df = pd.read_csv(r"CASHANTIR VU\Programs\Minors\IDA\Activities\Datasets\6Mednull_values.csv")

print("Original DataFrame:")
print(df)

# Identifying missing values
print("\nMissing values in the DataFrame:")
print(df.isnull().sum())

# Filling missing values in the 'Q1' column with the mean
df['Q1'].fillna(df['Q1'].mean(), inplace=True)

print("\nDataFrame after filling missing values in 'Q1' column:")
print(df)
