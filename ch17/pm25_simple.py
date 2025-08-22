import pandas as pd

df = pd.read_csv("https://data.epa.gov.tw/api/v2/aqx_p_02?api_key=e8dd42e6-9b8b-43f8-991e-b3dee723a52d&limit=1000&sort=datacreationdate%20desc&format=CSV")
while True:
    site = input('輸入測站名稱：')
    if len(site)>0:
        index = df.index[df['site']==site].tolist()
        if len(index)>0:
            n = int(index[0])
            print('{} 測站在 {} 的 PM2.5值為：{}'.format(site, df.iloc[n, 3], df.iloc[n, 2]))
        else:
            print('沒有 {} 測站！'.format(site))
    else:
        break
