import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv("6Med.csv")

# Scatter plot using Matplotlib
plt.scatter(df['Age'], df['BP'], color='blue')
plt.xlabel('Age')
plt.ylabel('Blood Pressure')
plt.title('Scatter Plot of Age vs BP (Matplotlib)')
plt.grid(True)
plt.show()

# Scatter plot using Seaborn
sns.scatterplot(x='Age', y='BP', data=df, color='green')
plt.title('Scatter Plot of Age vs BP (Seaborn)')
plt.xlabel('Age')
plt.ylabel('Blood Pressure')
plt.grid(True)
plt.show()
