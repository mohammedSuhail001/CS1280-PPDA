import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("6Med.csv")

# Compute correlation matrix for numeric columns
corr_matrix = df.corr(numeric_only=True)

# Set plot size and style
plt.figure(figsize=(10, 8))
sns.set(style="white")

# Create heatmap
sns.heatmap(corr_matrix, annot=True, cmap="YlGnBu", fmt=".2f", linewidths=0.5, square=True)

plt.title("Correlation Matrix Heatmap")
plt.show()
