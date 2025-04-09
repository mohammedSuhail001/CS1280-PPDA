import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("4laptops.csv")

# Boxplots using Matplotlib for all numerical columns
for col in df.select_dtypes(include=['number']).columns:
    plt.figure(figsize=(6, 4))
    plt.boxplot(df[col], notch=True, vert=False, patch_artist=True, widths=0.1)
    plt.xlabel(col)
    plt.title(f'Boxplot of {col} (Matplotlib)')
    plt.show()

# Boxplots using Seaborn for all numerical columns
for col in df.select_dtypes(include=['number']).columns:
    plt.figure(figsize=(6, 4))
    sns.boxplot(x=df[col])
    plt.title(f'Boxplot of {col} (Seaborn)')
    plt.show()
