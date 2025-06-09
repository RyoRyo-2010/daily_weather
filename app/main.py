import weather
import chat
import discord
import datetime
import dotenv
if __name__ == "__main__":
    print("daily_weather is starting...")
    dotenv.load_dotenv()

    # まず、天気予報を取得
    (setumei_text, chance_of_rains, teletop) = weather.get_weather()
    if setumei_text is None:
        print(f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')} 天気予報の取得に失敗しました。\n")
        exit(-1)

    # ChatGPTに投げる
    prompt = chat.create_prompt(setumei_text, chance_of_rains, teletop)
    print("できたてのプロンプト:" + prompt)

    response = chat.post_for_chatgpt(prompt)
    print("ChatGPTの応答:" + response)

    # discordに投げる
    message = f"おはようございます。今日は{datetime.datetime.now().strftime("%m月%d日")}です。山口県中部の天気をお伝えします。{response}\n" + \
    f"午前中の降水確率:{chance_of_rains["T06_12"]}、午後の降水確率:{chance_of_rains["T12_18"]}"
    discord.post_to_discord(message)