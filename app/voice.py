import requests

# テストできねえー！
VOICEVOX_URL = "http://voicevox:50021"

def synthesize(text, speaker=1, output_path="output.wav"):
    # 1. audio_query
    query_resp = requests.post(
        f"{VOICEVOX_URL}/audio_query",
        params={"text": text, "speaker": speaker}
    )
    query_resp.raise_for_status()
    audio_query = query_resp.json()

    # 2. synthesis
    synth_resp = requests.post(
        f"{VOICEVOX_URL}/synthesis",
        params={"speaker": speaker},
        json=audio_query
    )
    synth_resp.raise_for_status()

    # バイナリデータをファイルに保存
    with open(output_path, "wb") as f:
        f.write(synth_resp.content)

    print(f"音声ファイルを保存しました: {output_path}")
