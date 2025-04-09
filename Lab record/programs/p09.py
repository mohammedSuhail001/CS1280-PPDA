import pandas as pd

# Load the CSV file
df = pd.read_csv('lexperience.csv')

# Statistical summary of the data using describe()
description = df.describe()

# Calculating quantiles
quantiles = df['YearsExperience'].quantile([0.25, 0.5, 0.75])

# Calculating skewness and kurtosis
skewness = df['YearsExperience'].skew()
kurtosis = df['YearsExperience'].kurt()

# Calculating value counts for unique values in the 'YearsExperience' column
value_counts = df['YearsExperience'].value_counts()

# Displaying the results
print("Statistical Summary:\n", description)
print("\nQuantiles:\n", quantiles)
print("\nSkewness:", skewness)
print("Kurtosis:", kurtosis)
print("\nValue Counts:\n", value_counts)
