import pandas as pd
import numpy as np

# Load the CSV file
df = pd.read_csv('2Salary.csv')

# Statistical summary
description = df['YearsExperience'].describe()

# Calculating quantiles
quantiles = df['YearsExperience'].quantile([0.25, 0.5, 0.75])

# Calculating skewness and kurtosis
skewness = df['YearsExperience'].skew()
kurtosis = df['YearsExperience'].kurt()

# Displaying the results
print("Statistical Summary:\n", description)
print("\nQuantiles:\n", quantiles)
print("\nSkewness:", skewness)
print("Kurtosis:", kurtosis)
