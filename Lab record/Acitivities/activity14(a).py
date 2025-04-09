import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("5ds_salaries.csv")

# Histogram
sns.histplot(df["salary_in_usd"])
plt.title("Salary Distribution")
plt.xlabel("Salary in USD")
plt.ylabel("Count")
plt.show()

# Histogram with KDE
sns.histplot(df["salary_in_usd"], kde=True)
plt.title("Salary Distribution with KDE")
plt.xlabel("Salary in USD")
plt.show()

# Boxplot
sns.boxplot(x=df["salary_in_usd"])
plt.title("Boxplot of Salary in USD")
plt.xlabel("Salary in USD")
plt.show()
