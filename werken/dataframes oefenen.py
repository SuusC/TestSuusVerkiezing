import pandas as pd

df = pd.read_csv(r'C:\Users\suzan\Documents\traineeship\data\Uitslag_alle_gemeenten_TK20210317.csv', sep=';')
df2 = df[['RegioCode', 'RegioNaam']][15:18]  #[15:18] geeft alleen deze regels weer
print(df2)
#+print(df.head())
df3 = df.loc[1]
print(df3)

df4 = df.columns  #lijst van alle kolomtitels
print(df4)

# .type gebruiken om type te checken
