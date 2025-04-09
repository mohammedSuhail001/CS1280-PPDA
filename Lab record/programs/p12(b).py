#Let's first load the dataset to understand its structure and contents before proceeding with identifying outliers using IQR.

import pandas as pd

#Load the dataset 
data=pd.read_csv('4laptops.csv') 
data

q3=data['Weight_kg'].quantile(0.75)
q1=data['Weight_kg'].quantile(0.25)

iqr-q3-q1

lower_bound = q1 - 1.5*iqr
upper_bound=q3 + 1.5*iqr
outliers = data[(data['Weight_kg'] <lower_bound) | (data['Weight_kg'] > upper_bound)]
print('lower bound, upper bound and iqr values are: ',lower_bound, upper_bound, iqr)
print('No.of outliers are: ', outliers.shape[0])
