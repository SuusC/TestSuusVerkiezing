from flask import Flask
import pandas as pd

app = Flask(__name__)


@app.route("/provinciesgemeente",methods=['GET'])
def provincie_gemeente():
    df = pd.read_excel(r'C:\Users\suzan\Documents\traineeship\data\Gemeenten alfabetisch 2019.xls')
    prov_gem_df = df[['Gemeentenaam', 'Provincienaam']]
    prov_gem_html = prov_gem_df.to_html()
    return prov_gem_html


if __name__ == '__main__':
    app.run(port=8000)
