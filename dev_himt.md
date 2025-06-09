# 開発の道しるべ

## 実行環境
ただdocker execでやる。だってvoicevox使わないんだもん。

## 動作
このプログラムはDockerコンテナにされる。で、別のプログラムにより呼び出される。

まず~~OpenWeatherMap~~気象庁の非公式APIから天気を取得し、Chat GPTで要約する。それをVOICEVOXに渡して音声ファイル作成。
OpenWeatherMapはアカウント作成に制限があるため、ひとまず気象庁のやつで対応。

## ChatGPTにわたすプロンプト
- 今日の天気
- 朝8時から午後5時くらいまでで判断すること
- 天気概要(説明文)
- 6時間ごとの降水確率
- 1日の天気の要約(晴れ、とか曇のち雨、とか)
---

## 開発のヒント(Copilotにより作成された)

### アクセストークンの管理方法

- アクセストークンやAPIキーなどの機密情報は、**絶対にGitHubなどの公開リポジトリにプッシュしない**こと！
- `.gitignore` というファイルを使って、Gitで管理しないファイルやディレクトリを指定できる。
- 例えば、`config.env` などのファイルにトークンを保存し、`.gitignore` に `config.env` を追加しておくと安全。

#### 例

1. `.gitignore` ファイルを作成（または編集）して、以下を追加：
    ```
    config.env
    ```
2. `config.env` ファイルにトークンを記載（例）：
    ```
    OPENWEATHERMAP_API_KEY=xxxxxxxxxxxxxxxx
    CHATGPT_API_KEY=yyyyyyyyyyyyyyyyyyyyyy
    ```
3. プログラム内では `dotenv` などのライブラリを使って環境変数として読み込む。

### 参考

- `.gitignore` について:  
  https://git-scm.com/docs/gitignore
- Pythonで環境変数を使う方法:  
  https://pypi.org/project/python-dotenv/

---