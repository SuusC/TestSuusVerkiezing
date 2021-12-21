import pandas as pd
import landelijke_uitslag
import provincie_stemmen

def provincies_allemaal():
    df_landelijk = pd.read_csv(r'C:\Users\suzan\Documents\traineeship\data\Uitslag_alle_gemeenten_TK20210317.csv', sep=';')
    df_provincies = pd.read_excel(r'C:\Users\suzan\Documents\traineeship\data\Gemeenten alfabetisch 2019.xls')
    provincie_lijst = list(df_provincies['Provincienaam'].unique())
    totaalDF = pd.DataFrame()
    for provincie in provincie_lijst:
        tijdelijk_df = landelijke_uitslag.landelijke_uitslag(provincie_stemmen.provincie_stemmen(provincie))
        #df_renamed_provincie = tijdelijk_df.rename(columns={'stemmen': 'stemmen in ' + provincie, 'zetels': 'zetels in ' +provincie})
        df_renamed_provincie = tijdelijk_df.rename(columns={'zetels': 'zetels in ' + provincie})
        df_renamed_provincie = df_renamed_provincie.iloc[:,1]
        totaalDF = totaalDF.merge(df_renamed_provincie, how='outer', left_index=True, right_index=True)
    df_landelijke_uitslag = landelijke_uitslag.landelijke_uitslag(df_landelijk)
    df_renamed_landelijk = df_landelijke_uitslag.rename(columns={'zetels': 'zetels landelijk'})
    df_renamed_landelijk = df_renamed_landelijk.iloc[:,1]
    totaalDF2 = totaalDF.merge(df_renamed_landelijk, how='outer', left_index=True, right_index=True)
    totaalDF_sorteer = totaalDF2.sort_values(by= 'zetels landelijk', ascending=False)
    return totaalDF_sorteer