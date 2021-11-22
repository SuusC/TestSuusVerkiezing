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
    return "<p>Hello, World!</p>"

@app.route("/test",methods=['GET'])
def test():
    df = pd.read_csv(r'C:\Users\suzan\Documents\traineeship\data\Uitslag_alle_gemeenten_TK20210317.csv', sep=';')
    #d = pd.DataFrame(df)
    c = df.to_html()
    return c


if __name__ == '__main__':
    app.run(port=8000)

