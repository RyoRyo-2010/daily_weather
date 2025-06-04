import requests

def get_weather():
    URL = "https://weather.tsukumijima.net/api/forecast?city=350020"
    res = requests.get(URL)
    if res.status_code == 200:
        data = res.json()
        setumei_text = data["description"]["bodyText"] # 山口県は、高気圧...
        chance_of_rains = data["forecasts"][0]["chanceOfRain"] # n%の表記のリスト(length:たぶん4くらい)
        teletop = data["forecasts"][0]["detail"]["weather"] # 晴れ時々曇りとか
        return setumei_text, chance_of_rains, teletop
    else:
        print("天気予報の取得に失敗しました。")
        return None, None, None

