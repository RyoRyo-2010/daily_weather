import weather
import chat
import voice
import datetime
if __name__ == "__main__":
    print("daily_weather is starting...")
    # まず、天気予報を取得
    (setumei_text, chance_of_rains, teletop) = weather.get_weather()
    if setumei_text is None:
        print("天気予報の取得に失敗しました。")
        with open("error.log", "w") as f:
            f.write(f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')} 天気予報の取得に失敗しました。\n")
        exit(-1)
    # ChatGPT向けにテキストに手を加える
    # 無駄な改行を削除
    setumei_text = setumei_text.replace("\n\n", "\n")
    setumei_text = setumei_text.rstrip("\n")

    # ChatGPTに投げる
    prompt = chat.create_prompt(setumei_text, chance_of_rains, teletop)

    print("できたてのプロンプト:" + prompt)

    response = chat.post_for_chatgpt(prompt)
    print("ChatGPTの応答:" + response)

    # 思い切って音声合成してみる
    voice.synthesize(response, speaker=1, output_path=f"output.wav")
    print("音声合成が完了しました。output.wavに保存されました。")