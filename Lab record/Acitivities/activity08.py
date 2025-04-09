import pandas as pd

# Load the CSV file
df = pd.read_csv('2Salary.csv')

# Displaying the basic central tendencies and dispersion metrics
mean_value = df['Salary'].mean()
median_value = df['Salary'].median()
mode_value = df['Salary'].mode()[0]  # First mode if multiple exist
min_value = df['Salary'].min()
max_value = df['Salary'].max()
variance_value = df['Salary'].var()
std_dev_value = df['Salary'].std()

# Printing the results
print(f"Mean Salary: {mean_value}")
print(f"Median Salary: {median_value}")
print(f"Mode Salary: {mode_value}")
print(f"Minimum Salary: {min_value}")
print(f"Maximum Salary: {max_value}")
print(f"Salary Variance: {variance_value}")
print(f"Salary Standard Deviation: {std_dev_value}")
