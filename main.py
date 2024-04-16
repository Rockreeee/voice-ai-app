import voice_recognition as vc
import chat_gpt as gpt
import text_to_speech as speech

gpt_start_flag = True

# 対話の開始
while True:

    # 音声認識を実行
    recognized_text = vc.recognize_speech()
    print("You said: ", recognized_text)

    if recognized_text == "exit":
        speech.speak("Thank you")
        break

    if recognized_text == "stop":
        speech.speak("GPT stop")
        gpt_start_flag = False

    # gptの動作許可がある場合は動く
    if gpt_start_flag and recognized_text != "":
        # chat gptに入力
        user_input = recognized_text
        response = gpt.interact_with_chatgpt(user_input)
        print("Gpt said: ", response)

        # テキストを音声に変換して再生
        speech.speak(response)

    if recognized_text == "start":
        speech.speak("GPT start")
        gpt_start_flag = True



