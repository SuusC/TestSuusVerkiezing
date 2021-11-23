from flask import Flask
import pandas as pd


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
    #antwoord = gemeente + "<br>\n Percentage ongeldig: " + str(percentageongeldig) + "<br>\n Percentage geldig: " \
    #           + str(percentagegeldig)
    #return antwoord
    geldig2df = pd.DataFrame(data={'Gemeente': gemeente, 'Percentage Geldig': percentagegeldig,
                                   'Percentage Ongeldig': percentageongeldig}, index=["1"])
    geldig2html = geldig2df.to_html()
    return geldig2html

#@app.route("/landelijkeuitslag",methods=['GET'])
#def landelijke_uitslag():





if __name__ == '__main__':
    app.run(port=8000)


