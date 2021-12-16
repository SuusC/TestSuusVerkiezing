import pandas as pd
def provincie_stemmen(provincie):
    df_uitslagen = pd.read_csv(r'C:\Users\suzan\Documents\traineeship\data\Uitslag_alle_gemeenten_TK20210317.csv',
                               sep=';')
    uitslagenDF = df_uitslagen
    df_provincies = pd.read_excel(r'C:\Users\suzan\Documents\traineeship\data\Gemeenten alfabetisch 2019.xls')

    prov_gem_df = pd.DataFrame(data=list(df_provincies['Provincienaam']), columns=['Provincienaam'], index=list(df_provincies['Gemeentenaam']))
    prov_gem_df.index.name = 'Gemeentenaam'

    #print(prov_gem_df)

    df_merge = pd.merge(df_uitslagen, df_provincies, how='left', left_on=['RegioNaam'], right_on=['Gemeentenaam'])
    #print(df_met_provincies)

    df_provincie = df_merge[df_merge['Provincienaam'] == provincie ]
    df_provincie2 = df_provincie.iloc[:,0:47]
    return df_provincie2
