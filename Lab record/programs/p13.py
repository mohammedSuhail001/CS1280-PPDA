# Importing required libraries
import pandas as pd

# Creating the employee_details DataFrame
employee_details = pd.DataFrame({
    'EmployeeID': [101, 102, 103, 104, 105],
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Department': ['HR', 'Engineering', 'Engineering', 'HR', 'Marketing']
})

# Creating the employee_salaries DataFrame
employee_salaries = pd.DataFrame({
    'EmployeeID': [101, 102, 103, 104, 105],
    'Salary': [50000, 70000, 80000, 55000, 60000]
})

# Creating the sales_region_1 DataFrame
sales_region_1 = pd.DataFrame({
    'Date': pd.date_range(start='2024-01-01', periods=5, freq='D'),
    'Region': ['North'] * 5,
    'Sales': [250, 300, 200, 400, 350]
})

# Creating the sales_region_2 DataFrame
sales_region_2 = pd.DataFrame({
    'Date': pd.date_range(start='2024-01-01', periods=5, freq='D'),
    'Region': ['South'] * 5,
    'Sales': [300, 320, 280, 360, 310]
})

# Display the datasets
print("Employee Details:")
print(employee_details)

print("\nEmployee Salaries:")
print(employee_salaries)

print("\nSales Region 1:")
print(sales_region_1)

print("\nSales Region 2:")
print(sales_region_2)

# Grouping by department and calculating average salary
avg_salary_per_dept = employee_details.merge(employee_salaries, on='EmployeeID') \
    .groupby('Department')['Salary'].mean()

print("\nAverage Salary per Department:")
print(avg_salary_per_dept)

# Merging two DataFrames on the EmployeeID column
merged_data = pd.merge(employee_details, employee_salaries, on='EmployeeID', how='inner')

print("\nMerged Employee Data:")
print(merged_data)

# Creating the stock_prices DataFrame with 'Date' as the index
stock_prices = pd.DataFrame({
    'Date': pd.date_range(start='2024-01-01', periods=5, freq='D'),
    'Price': [150, 155, 152, 158, 160]
})
stock_prices.set_index('Date', inplace=True)

# Creating the market_volume DataFrame with 'Date' as the index
market_volume = pd.DataFrame({
    'Date': pd.date_range(start='2024-01-01', periods=5, freq='D'),
    'Volume': [1000, 1100, 1050, 1150, 1200]
})
market_volume.set_index('Date', inplace=True)

print("\nStock Prices Data:")
print(stock_prices)

print("\nMarket Volume Data:")
print(market_volume)

# Joining market_volume to stock_prices based on their index
joined_data = stock_prices.join(market_volume, how='inner')

print("\nJoined Stock Prices and Market Volume Data:")
print(joined_data)

# Concatenating DataFrames vertically
consolidated_sales = pd.concat([sales_region_1, sales_region_2], axis=0)

print("\nConsolidated Sales Data:")
print(consolidated_sales)
