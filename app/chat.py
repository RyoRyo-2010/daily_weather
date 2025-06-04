from openai import OpenAI
from datetime import datetime

def create_prompt(setumei_text, chance_of_rains, teletop):
    """
    ChatGPTに投げるプロンプトを作成する関数
    """
    # 'T00_06': '--%', 'T06_12': '--%', 'T12_18': '--%', 'T18_24': '0%'}

    today_str = datetime.now().strftime("Today is %-m/%-d.")
    prompt = f"""
    {today_str}
    You are a weather forecast expert.
    Summarize the weather forecast for today between 8am and 5pm in simple Japanese.
    Example: "今日は1日を通してよく晴れるでしょう" or "お昼から雨が降るようです".
    Weather agency explanation: 「{setumei_text}」
    Chance of rain from 6am to 12pm(--% means sunny): {chance_of_rains["T06_12"]}
    Chance of rain from 12pm to 6pm(--% means sunny): {chance_of_rains["T12_18"]}
    Today's weather: {teletop}
    Based on this information, write a concise explanation in JAPANESE.簡潔に！
    """
    return prompt.strip()  # 不要な空白を削除して返す

def post_for_chatgpt(prompt):
    """
    ChatGPTにプロンプトを投げて、応答を取得する関数
    """
    # ここでは、ChatGPT APIを呼び出すコードを実装する必要があります。
    # 例えば、requestsライブラリを使ってPOSTリクエストを送信するなど。
    # ただし、この関数の実装は省略します。
    client = OpenAI()

    response = client.responses.create(
        model="o4-mini",
        input=prompt,
        # limit=40  # 必要に応じて調整
    )

    return response.output_text