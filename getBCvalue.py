import requests

def getBCvalue():
    r = requests.get('https://api.bitflyer.jp/v1/ticker?product_code=BTC_JPY')
    json = r.json()
    return json["ltp"]
