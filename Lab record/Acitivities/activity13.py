import pandas as pd

# Employee Details
employee_details = pd.DataFrame({
    'EmployeeID': [101, 102, 103, 104, 105],
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Department': ['HR', 'Engineering', 'Engineering', 'HR', 'Marketing']
})

# Employee Salaries
employee_salaries = pd.DataFrame({
    'EmployeeID': [101, 102, 103, 104, 105],
    'Salary': [50000, 70000, 80000, 55000, 60000]
})

# Region 1 Sales
sales_region_1 = pd.DataFrame({
    'Date': pd.date_range(start='2024-01-01', periods=5, freq='D'),
    'Region': ['North'] * 5,
    'Sales': [250, 300, 200, 400, 350]
})

# Region 2 Sales
sales_region_2 = pd.DataFrame({
    'Date': pd.date_range(start='2024-01-01', periods=5, freq='D'),
    'Region': ['South'] * 5,
    'Sales': [300, 320, 280, 360, 310]
})

# GroupBy with Median Salary per Department
merged_df = employee_details.merge(employee_salaries, on='EmployeeID')
median_salary = merged_df.groupby('Department')['Salary'].median()

print("\n▶ Median Salary per Department:")
print(median_salary)

# Outer merge to include all employee records, even if salary or detail is missing
outer_merged = pd.merge(employee_details, employee_salaries, on='EmployeeID', how='outer')
print("\n▶ Outer Merged Data (Employee Details + Salaries):")
print(outer_merged)

# Creating stock_prices DataFrame and setting 'Date' as index
stock_prices = pd.DataFrame({
    'Date': pd.date_range(start='2024-01-01', periods=5, freq='D'),
    'Price': [150, 155, 152, 158, 160]
}).set_index('Date')

# Creating market_volume DataFrame and setting 'Date' as index
market_volume = pd.DataFrame({
    'Date': pd.date_range(start='2024-01-01', periods=5, freq='D'),
    'Volume': [1000, 1100, 1050, 1150, 1200]
}).set_index('Date')

# Joining stock_prices and market_volume on 'Date' index
joined_df = stock_prices.join(market_volume, how='inner')
print("\n▶ Joined Data (Stock Prices + Market Volume):")
print(joined_df)

# Horizontal concatenation: adding South region's sales as a new column beside North region
horizontal_concat = pd.concat([sales_region_1.reset_index(drop=True), 
                               sales_region_2[['Sales']].rename(columns={'Sales': 'South_Sales'})], axis=1)

print("\n▶ Horizontally Concatenated Sales Data:")
print(horizontal_concat)
