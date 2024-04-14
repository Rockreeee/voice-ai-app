import speech_recognition as sr

def recognize_speech():
    # 音声認識器のインスタンスを作成
    recognizer = sr.Recognizer()

    try:
        # マイクから音声を取得
        with sr.Microphone() as source:
            print("Please speak something...")
            audio = recognizer.listen(source)

        # 音声をテキストに変換
        text = recognizer.recognize_google(audio, language="en-US")
        return text
    except sr.UnknownValueError:
        print("Sorry, could not understand audio.")
        return ""
    except sr.RequestError as e:
        print("Error fetching results; {0}".format(e))
        return ""

