from gtts import gTTS
import pygame
from tempfile import TemporaryFile

# テキストを音声に変換して再生する関数を定義
def speak(text):
    tts = gTTS(text=text, lang="en")  # テキストを英語としてGoogle Text-to-Speech APIに送信
    temp_file = TemporaryFile()  # 一時ファイルを作成
    tts.write_to_fp(temp_file)  # 音声ファイルを一時ファイルに書き込む
    temp_file.seek(0)  # ファイルポインタを先頭に戻す

    pygame.mixer.init()  # Pygameの初期化
    pygame.mixer.music.load(temp_file)  # 音声ファイルを読み込む
    pygame.mixer.music.play()  # 音声を再生
    while pygame.mixer.music.get_busy():  # 再生中は待機
        continue
    temp_file.close()  # 一時ファイルを閉じる

