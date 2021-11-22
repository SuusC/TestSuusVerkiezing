import pandas as pd


df = pd.read_csv(r'C:\Users\suzan\Documents\traineeship\data\Uitslag_alle_gemeenten_TK20210317.csv', sep=';')
f = (df[['RegioNaam','VVD']])
g = f.sort_values(by=['VVD'])
print(g)

