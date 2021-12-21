from flask import Flask
import pandas as pd
import landelijke_uitslag
import provincie_stemmen
import provincies_allemaal

app = Flask(__name__)


@app.route("/",methods=['GET'])
def hello_world():
    with open(r'C:\Users\suzan\Documents\traineeship\data\Uitslag_alle_gemeenten_TK20210317.csv', 'r',
              encoding='utf-8') as f:
        b = f.readline().split(';')
        a = ('\n<br>'.join(b))
        return a


@app.route("/test",methods=['GET'])
def test():
    df = pd.read_csv(r'C:\Users\suzan\Documents\traineeship\data\Uitslag_alle_gemeenten_TK20210317.csv', sep=';')
    c = df.to_html()
    return c

@app.route("/start",methods=['GET'])
def hoi():
    return "hoi"

@app.route("/vvd",methods=['GET'])
def vvdamsterdam():
    df = pd.read_csv(r'C:\Users\suzan\Documents\traineeship\data\Uitslag_alle_gemeenten_TK20210317.csv', sep=';')
    d = (df['VVD'][15])
    e = str(d)
    return e

@app.route("/rangschikking/vvd",methods=['GET'])
def rangschikking():
    df = pd.read_csv(r'C:\Users\suzan\Documents\traineeship\data\Uitslag_alle_gemeenten_TK20210317.csv', sep=';')
    f = (df[['RegioNaam', 'VVD']])
    g = f.sort_values(by=['VVD'], ascending=False)
    h = g.to_html()
    return h

@app.route("/rangschikking/<partij>",methods=['GET'])
def rangschikking2(partij='VVD'):
    df = pd.read_csv(r'C:\Users\suzan\Documents\traineeship\data\Uitslag_alle_gemeenten_TK20210317.csv', sep=';')
    i = (df[['RegioNaam', partij]])
    j = i.sort_values(by=[partij], ascending=False)
    k = j.to_html()
    return k

@app.route("/geldig",methods=['GET'])
def geldig():
    df = pd.read_csv(r'C:\Users\suzan\Documents\traineeship\data\Uitslag_alle_gemeenten_TK20210317.csv', sep=';')
    ongeldiglijst = list(df['OngeldigeStemmen'])
    geldiglijst = list(df['GeldigeStemmen'])
    regiolijst = list(df['RegioNaam'])
    percentageongeldig = list((df['OngeldigeStemmen']/df['Opkomst'])*100)
    geldigdf = pd.DataFrame(data={'Regio Naam': regiolijst,'Ongeldige Stemmen' : ongeldiglijst,
                                  'Geldige Stemmen' : geldiglijst, 'Percentage Ongeldige Stemmen' : percentageongeldig})
    sorteergeldigdf = geldigdf.sort_values(by=['Percentage Ongeldige Stemmen'], ascending=False)
    geldightml = sorteergeldigdf.to_html()
    return geldightml

@app.route("/geldig/<gemeente>",methods=['GET'])
def geldig2(gemeente='Oisterwijk'):
    df = pd.read_csv(r'C:\Users\suzan\Documents\traineeship\data\Uitslag_alle_gemeenten_TK20210317.csv', sep=';')
    rijgemeente = df[df['RegioNaam'] == gemeente].index[0]
    percentageongeldig = round((df.loc[rijgemeente, 'OngeldigeStemmen'] / df.loc[rijgemeente,'Opkomst']) * 100, 2)
    percentagegeldig = round((df.loc[rijgemeente, 'GeldigeStemmen'] / df.loc[rijgemeente, 'Opkomst']) * 100, 2)
    geldig2df = pd.DataFrame(data={'Gemeente': gemeente, 'Percentage Geldig': percentagegeldig,
                                   'Percentage Ongeldig': percentageongeldig}, index=["1"])
    geldig2html = geldig2df.to_html()
    return geldig2html

# 16-12 uitslagen per provincies gaan proberen




@app.route("/provincies/<provincie>",methods=['GET'])
def provincie_als_landelijk(provincie=''):
    return landelijke_uitslag.landelijke_uitslag(provincie_stemmen.provincie_stemmen(provincie)).to_html()


#provincie_als_landelijk(provincie='')

@app.route("/provincies",methods=['GET'])
def provincies_allemaal3():
    antwoord = provincies_allemaal.provincies_allemaal()
    return antwoord.to_html()

@app.route("/provincies/weging",methods=['GET'])
def provincies_allemaal2(inputDrenthe=1, inputNoord_Holland=1, inputGelderland=1, inputFriesland=1, inputZuid_Holland=1,
                            inputOverijssel=1, inputFlevoland=1, inputNoord_Brabant=1, inputUtrecht=1, inputGroningen=1,
                            inputLimburg=1, inputZeeland=1):
    df_landelijk = pd.read_csv(r'C:\Users\suzan\Documents\traineeship\data\Uitslag_alle_gemeenten_TK20210317.csv', sep=';')
    df_provincies = pd.read_excel(r'C:\Users\suzan\Documents\traineeship\data\Gemeenten alfabetisch 2019.xls')
    provincie_lijst = list(df_provincies['Provincienaam'].unique())
    totaalDF = pd.DataFrame()
    for provincie in provincie_lijst:
        tijdelijk_df = landelijke_uitslag.landelijke_uitslag(provincie_stemmen.provincie_stemmen(provincie))
        #df_renamed_provincie = tijdelijk_df.rename(columns={'stemmen': 'stemmen in ' + provincie, 'zetels': 'zetels in ' +provincie})
        df_renamed_provincie = tijdelijk_df.rename(columns={'stemmen': 'stemmen in ' + provincie})
        df_renamed_provincie = df_renamed_provincie.iloc[:,0]
        totaalDF = totaalDF.merge(df_renamed_provincie, how='outer', left_index=True, right_index=True)
    df_landelijke_uitslag = landelijke_uitslag.landelijke_uitslag(df_landelijk)
    df_renamed_landelijk = df_landelijke_uitslag.rename(columns={'stemmen': 'stemmen landelijk'})
    df_renamed_landelijk = df_renamed_landelijk.iloc[:,0]
    totaalDF2 = totaalDF.merge(df_renamed_landelijk, how='outer', left_index=True, right_index=True)
    totaalDF_sorteer = totaalDF2.sort_values(by= 'stemmen landelijk', ascending=False)
    totaalstemmen_perkolom = totaalDF_sorteer.sum()
    gewichten_series = totaalstemmen_perkolom/totaalstemmen_perkolom[12]
    gewichten_series_zonder_landelijk = gewichten_series[:12]
    series_input_wegingen = pd.Series([inputDrenthe, inputNoord_Holland, inputGelderland, inputFriesland, inputZuid_Holland,
                            inputOverijssel, inputFlevoland, inputNoord_Brabant, inputUtrecht, inputGroningen,
                            inputLimburg, inputZeeland], index=gewichten_series_zonder_landelijk.index)
    #print(series_input_wegingen)
    gewichten_series_keer_inputwegingen = gewichten_series_zonder_landelijk*series_input_wegingen
    print(gewichten_series_keer_inputwegingen)

    df_provincies = provincies_allemaal.provincies_allemaal()
    df_provincies_zonder_landelijk = df_provincies.iloc[:,:12]
    test = df_provincies_zonder_landelijk.dot(gewichten_series_keer_inputwegingen.to_numpy())
    test2 = test.to_frame()
    test3 = test2/test2.sum()*150
    print(test3)
    #print(test3.sum())
    return(test3.to_html())
provincies_allemaal2(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)


if __name__ == '__main__':
    app.run(port=8000)


