import dotenv
import os
import requests
import json

def post_to_discord(message):
    dotenv.load_dotenv()
    URL = os.environ["DISCORD_WEBHOOK_URL"]
    
    
    payload = json.dumps({
    "content": message
    })
    headers = {
    'Content-Type': 'application/json'
    }

    response = requests.request("POST", URL, headers=headers, data=payload)


