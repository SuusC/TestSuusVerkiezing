import pandas as pd

df_gemverkoopprijs = pd.read_csv(r'C:\Users\suzan\Documents\traineeship\casebigdata\gem_verkoopprijs.csv', sep = ",")

print(df_gemverkoopprijs.head(2))

df_transactie_vs_vraagprijs = pd.read_csv(r'C:\Users\suzan\Documents\traineeship\casebigdata\transactie_vs_vraagprijs.csv')

print(df_transactie_vs_vraagprijs.head(2))

new_df = pd.merge(df_gemverkoopprijs, df_transactie_vs_vraagprijs, how='left', left_on=['GemNaam'], right_on=['GemNaam'])

print(new_df.columns)
print(new_df.head())