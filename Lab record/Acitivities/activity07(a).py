import pandas as pd

# Creating a list of dictionaries with product information
data = [
    {'Product Name': 'Laptop', 'Category': 'Electronics', 'Price': 1000},
    {'Product Name': 'Phone', 'Category': 'Electronics', 'Price': 500},
    {'Product Name': 'Shoes', 'Category': 'Fashion', 'Price': 80},
    {'Product Name': 'Watch', 'Category': 'Accessories', 'Price': 150}
]

# Creating a DataFrame
df = pd.DataFrame(data)

# Adding a new column 'Discounted Price' (90% of the original price)
df['Discounted Price'] = df['Price'] * 0.90

# Displaying the DataFrame
print(df)
