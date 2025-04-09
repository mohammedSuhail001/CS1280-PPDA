import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("5ds_salaries.csv")

# Optional: Select only numeric columns for pairplot
numeric_df = df.select_dtypes(include=["int64", "float64"])

# Create the pair plot
sns.pairplot(numeric_df)
plt.suptitle("Pair Plot of Numeric Columns", y=1.02)
plt.show()
