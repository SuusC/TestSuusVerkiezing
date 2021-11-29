import pandas as pd
df = pd.read_csv(r'C:\Users\suzan\Documents\traineeship\data\Uitslag_alle_gemeenten_TK20210317.csv', sep=';')

#invoer = input()
#print(df.loc[4, 'VVD':'De Groenen'])

df2 = df[['RegioNaam', 'VVD', 'D66', 'PVV (Partij voor de Vrijheid)', 'CDA', 'SP (Socialistische Partij)',
          'Partij van de Arbeid (P.v.d.A.)', 'GROENLINKS', 'Forum voor Democratie', 'Partij voor de Dieren',
          'ChristenUnie', 'Volt', 'JA21', 'Staatkundig Gereformeerde Partij (SGP)', 'DENK', '50PLUS', 'BBB',
          'BIJ1', 'CODE ORANJE', 'NIDA', 'Splinter', 'Piratenpartij', 'JONG', 'Trots op Nederland (TROTS)',
          'Lijst Henk Krol', 'NLBeter', 'Blanco (Zeven, A.J.L.B.)', 'LP (Libertaire Partij)', 'OPRECHT', 'JEZUS LEEFT',
          'DE FEESTPARTIJ (DFP)', 'U-Buntu Connected Front', 'Vrij en Sociaal Nederland', 'Partij van de Eenheid',
          'Wij zijn Nederland', 'Partij voor de Republiek', 'Modern Nederland', 'De Groenen']]

print(df2)

#iets met .isnull




#eerste_df = pd.DataFrame(data={'Regio Naam': })
#print(eerste_df)
