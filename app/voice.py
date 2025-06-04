import requests
import os

VOICEVOX_URL = "http://voicevox:50021"

def get_audio_query(text, speaker=1):
    """
    VOICEVOXエンジンのaudio_query APIを呼び出し、音声合成用クエリを取得する
    """
    resp = requests.post(
        f"{VOICEVOX_URL}/audio_query",
        params={"text": text, "speaker": speaker}
    )
    resp.raise_for_status()
    return resp.json()

def synthesize(text, speaker=1, output_path="data/output.wav"):
    """
    テキストをVOICEVOXで音声合成し、WAVファイルとして保存する
    """

    # ディレクトリが存在しない場合は作成
    output_dir = os.path.dirname(output_path)
    if output_dir and not os.path.exists(output_dir):
        os.makedirs(output_dir, exist_ok=True)

    audio_query = get_audio_query(text, speaker)
    resp = requests.post(
        f"{VOICEVOX_URL}/synthesis",
        params={"speaker": speaker},
        json=audio_query
    )
    resp.raise_for_status()
    with open(output_path, "wb") as f:
        f.write(resp.content)
    print(f"音声ファイルを保存しました: {output_path}")
