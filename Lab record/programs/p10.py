import pandas as pd
df = pd.read_csv('4laptops.csv')
df

# Onehot encoding without sci-kit learn library
pd.get_dummies(df)
from sklearn.preprocessing import OneHotEncoder

# creating instance of one-hot-encoder
enc = OneHotEncoder()
enc_data = enc.fit_transform(df[['Category']])
enc_data # gives an object as output

# Identifying the list of categories, one-hot encoding is considering as columns
enc.categories_
enc_data.toarray() # converting object into array using toarray function

#creating a dataframe without giving column names
enc_df = pd.DataFrame(enc_data.toarray())
enc_df

# creating a dataframe with giving column names
enc_df = pd.DataFrame(enc_data.toarray(), columns=['2 in 1 Convertible', 'Gaming', 'Netbook', 'Notebook', 'Ultrabook', 'Workstation'])
enc_df
df1 = df.join(enc_df) # joining df and enc_df
df1

# Using label encoding
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()

# Fit and transform the data
df['RAM'] = le.fit_transform(df['RAM'])
df

le.classes_
