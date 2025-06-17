import dotenv
import os
import requests
import json

def post_to_discord(message):
    URL = os.environ["DISCORD_WEBHOOK_URL"]
    
    
    payload = json.dumps({
    "content": message
    })
    headers = {
    'Content-Type': 'application/json'
    }

    response = requests.request("POST", URL, headers=headers, data=payload)

def weather_to_icon(weather_type):
    keys = [{"weather":"晴","icon":":sunny:"}]
    for key in keys:
        if(key["weather"] == weather_type):
            return key["icon"]
    
    return f"未定義です。\nweather_type=`{weather_type:weather_type}`"