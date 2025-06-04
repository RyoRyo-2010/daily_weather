# daily_weather

## 概要
毎朝、気象庁から取得した天気予報を生成AIが要約して音声合成で伝えます。

## インストール方法
事前にDockerをインストールしておきます。

`.env`に、`OPENAI_API_KEY="<YOUR_KEY_IS_HERE>"`という風にOpenAIのアクセストークンを設定します。

レポジトリをcloneして、`cd app`してから`docker compose up -d`で準備完了です。

音声を生成して欲しいときに`docker compose exec daily_weather python3 /daily_weather/app/main.py`を実行すると、`app/data`に音声ファイルが生成されます。

## 使用サービス

### 音声合成
[VOICEVOX](https://voicevox.hiroshiba.jp/)を使用しています。

VOICEVOX:ずんだもん

### 天気予報
[天気予報 API（livedoor 天気互換）](https://weather.tsukumijima.net/)を使用しました。このデータは気象庁から提供されています。

### 生成AI
[OpenAI Python API library](https://github.com/openai/openai-python)を使っています。