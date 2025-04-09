import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv("6Med.csv")

# View column names to decide which variables to plot
print(df.columns)

# Assuming 'Age' and 'BP' (Blood Pressure) are present in your dataset

# Matplotlib Line Chart
plt.plot(df['Age'], df['BP'], marker='o', label='BP over Age')
plt.xlabel('Age')
plt.ylabel('Blood Pressure')
plt.title('Trend of BP over Age (Matplotlib)')
plt.legend()
plt.grid(True)
plt.show()

# Seaborn Line Plot
sns.lineplot(x='Age', y='BP', data=df, marker='o')
plt.title('Trend of BP over Age (Seaborn)')
plt.xlabel('Age')
plt.ylabel('Blood Pressure')
plt.grid(True)
plt.show()
