# Voice AI App

## Features

音声対話型のアプリです。

pythonを用いて、以下のフローで動作します。

1. speech_recognitionで音声を認識し、テキスト化
2. chat gptで返答を作成
3. gttsで読み上げ


## Requirement

* python環境
* Chat GPT アカウント


voice_recognition.pyを動作させるためのライブラリ
- bportaudio
- pyaudio
- flac

test_to_speech.pyを動作させるためのライブラリ
- pygame

同階層内にsetting.pyファイルを作成し以下を追加してください
```
chat_gpt_api_key = "***"
```
(***には自身のchat gptのapiキーを入力してください)

## Usage


```zsh
git clone https://github.com/hoge/~
cd ~
python main.py
```



## Note

使用は自己責任です

<!-- # Author

作成情報を列挙する

* 作成者
* 所属
* E-mail

# License
ライセンスを明示する

"hoge" is under [MIT license](https://en.wikipedia.org/wiki/MIT_License). -->
