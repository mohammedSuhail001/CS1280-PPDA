import pandas as pd
from sklearn.preprocessing import OneHotEncoder, LabelEncoder

# Load the dataset
df = pd.read_csv('laptops.csv')

# One-hot encoding for 'Operating System' column
one_hot_enc = OneHotEncoder()
os_encoded = one_hot_enc.fit_transform(df[['Operating System']])

# Creating a DataFrame with OneHotEncoded columns
os_encoded_df = pd.DataFrame(os_encoded.toarray(), columns=one_hot_enc.categories_[0])

# Joining the original dataframe with the encoded OS columns
df = df.join(os_encoded_df).drop(columns=['Operating System'])

# Label encoding for 'Storage' column
label_enc = LabelEncoder()
df['Storage'] = label_enc.fit_transform(df['Storage'])

# Display the updated DataFrame
print(df)
