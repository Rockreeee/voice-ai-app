import requests
import setting

def interact_with_chatgpt(prompt):
    # ChatGPTのAPIエンドポイント
    api_endpoint = "https://api.openai.com/v1/chat/completions"
    # OpenAI APIキー
    api_key = setting.chat_gpt_api_key

    # リクエストのヘッダー
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    # リクエストボディ
    data = {
        "model": "gpt-3.5-turbo",
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": 100
    }

    # APIエンドポイントにリクエストを送信
    response = requests.post(api_endpoint, json=data, headers=headers)

    # レスポンスのJSONデータを取得
    response_json = response.json()

    # print(response_json)

    # APIからの応答を返す
    return response_json['choices'][0]['message']['content']
