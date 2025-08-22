from flask import Flask
app = Flask(__name__)

import pandas as pd
import urllib

@app.route('/pm25/<site>')
def pm25(site):
    site = urllib.parse.unquote(site)
    df = pd.read_csv("https://data.epa.gov.tw/api/v2/aqx_p_02?api_key=e8dd42e6-9b8b-43f8-991e-b3dee723a52d&limit=1000&sort=datacreationdate%20desc&format=CSV")
    index = df.index[df['site']==site].tolist()
    if len(index)>0:
        n = int(index[0])
        reStr = '{'
        reStr += '"測站":"{}", "PM2.5":"{}", "時間":"{}"'.format(site, df.iloc[n, 2], df.iloc[n, 3])
        reStr += '}'
    else:
        reStr = '沒有 {} 測站！'.format(site)
    return reStr

if __name__ == '__main__':
    app.run()

