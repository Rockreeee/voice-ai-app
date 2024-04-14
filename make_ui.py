import tkinter as tk

def set_ui(root):
    root.title("Voice Chat")

    # 画面サイズの取得
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # ウィンドウの幅を画面幅と同じに設定
    window_width = screen_width
    # ウィンドウの高さを画面高さの25%に設定
    window_height = int(screen_height * 0.25)

    # ウィンドウのサイズと位置を設定
    root.geometry("{}x{}+0+{}".format(window_width, window_height, screen_height - window_height))

def show_conversation(root, conversation):
    # ラベルのフォントと色を設定
    label_font = ("Helvetica", 36)  # フォントとサイズを指定

    conversation_label = tk.Label(root, text=conversation[0], font=label_font, fg="grey")
    conversation_label.pack(pady=20)

    if len(conversation) == 2:
        conversation_label = tk.Label(root, text=conversation[1], font=label_font, fg="white")
    conversation_label.pack(pady=20)
