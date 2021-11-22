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
def rankschikking():
    df = pd.read_csv(r'C:\Users\suzan\Documents\traineeship\data\Uitslag_alle_gemeenten_TK20210317.csv', sep=';')
    f = (df[['RegioNaam', 'VVD']])
    g = f.sort_values(by=['VVD'])
    h = g.to_html()
    return (h)



if __name__ == '__main__':
    app.run(port=8000)

