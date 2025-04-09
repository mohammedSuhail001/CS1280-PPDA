import pandas as pd
from sklearn.preprocessing import StandardScaler, Normalizer, MinMaxScaler

df = pd.read_csv(r"3Salary_Data.csv")

scaler = StandardScaler()
normalizer = Normalizer()
minmax_scaler = MinMaxScaler()

scaled_data = scaler.fit_transform(df)
scaled_df1 = pd.DataFrame(scaled_data, columns=df.columns)

normalized_data = normalizer.fit_transform(df)
normalized_df = pd.DataFrame(normalized_data, columns=df.columns)

minmax_scaled_data = minmax_scaler.fit_transform(df)
minmax_scaled_df = pd.DataFrame(minmax_scaled_data, columns=df.columns)

display(scaled_df1, normalized_df, minmax_scaled_df)
