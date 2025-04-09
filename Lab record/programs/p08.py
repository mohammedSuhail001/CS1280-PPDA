import pandas as pd

# Load the CSV file
df = pd.read_csv('lexperience.csv')

# Displaying the basic central tendencies and dispersion metrics
mean_value = df['YearsExperience'].mean()
median_value = df['YearsExperience'].median()
mode_value = df['YearsExperience'].mode()[0]  # First mode if multiple exist
min_value = df['YearsExperience'].min()
max_value = df['YearsExperience'].max()
variance_value = df['YearsExperience'].var()
std_dev_value = df['YearsExperience'].std()

# Printing the results
print(f"Mean: {mean_value}")
print(f"Median: {median_value}")
print(f"Mode: {mode_value}")
print(f"Minimum: {min_value}")
print(f"Maximum: {max_value}")
print(f"Variance: {variance_value}")
print(f"Standard Deviation: {std_dev_value}")
