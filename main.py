import weather
import chat
import weather

if __name__ == "__main__":
    print("daily_weather is starting...")
    # まず、天気予報を取得
    (setumei_text, chance_of_rains, teletop) = weather.get_weather()
    if setumei_text is None:
        print("天気予報の取得に失敗しました。")
        exit(-1)
    # ChatGPT向けにテキストに手を加える
    # 無駄な改行を削除
    setumei_text = setumei_text.replace("\n\n", "\n")
    setumei_text = setumei_text.rstrip("\n")

    # ChatGPTに投げる
    prompt = chat.create_prompt(setumei_text, chance_of_rains, teletop)

    print("できたてのプロンプト:" + prompt)