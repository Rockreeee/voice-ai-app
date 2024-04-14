import speech_recognition as sr

def record_audio():
    # 音声認識器のインスタンスを作成
    recognizer = sr.Recognizer()

    # マイクから音声を録音
    with sr.Microphone() as source:
        print("Please speak something...")

        # バックグラウンドノイズのレベルを調整
        recognizer.adjust_for_ambient_noise(source)

        # 音声の最初の1秒間にバックグラウンドノイズを検出し、それを除去します
        audio = recognizer.listen(source, timeout=None, phrase_time_limit=None)

    return audio

def transcribe_audio(audio):
    # 音声をテキストに変換
    try:
        text = recognizer.recognize_google(audio, language="en-US")
        return text
    except sr.UnknownValueError:
        print("Sorry, could not understand audio.")
        return ""
    except sr.RequestError as e:
        print("Error fetching results; {0}".format(e))
        return ""

# 音声認識器のインスタンスを作成
recognizer = sr.Recognizer()

# 音声の録音
audio = record_audio()

# 録音した音声をテキストに変換
text = transcribe_audio(audio)

print("You said:", text)
