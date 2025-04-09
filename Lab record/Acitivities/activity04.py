import pandas as pd

def process_csv(file_path):
    # Read the CSV file
    df = pd.read_csv(file_path)
    
    # Display the last 3 rows
    print("Last 3 rows:")
    print(df.tail(3))
    
    # Display the description and information of the DataFrame
    print("\nDataFrame Description:")
    print(df.describe())
    
    print("\nDataFrame Information:")
    print(df.info())
    
    # Display column names
    print("\nColumn Names:")
    print(df.columns.tolist())

# Example usage
file_path = "your_file.csv"  # Replace with your CSV file path
process_csv(file_path)
