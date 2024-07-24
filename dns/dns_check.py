
import tkinter as tk
from generate_url import generate_url

def on_generate_button_click():
    base_url = entry_base_url.get()
    path = entry_path.get()
    query = entry_query.get()
    generate_url(base_url, path, query)

# Tkinterのウィンドウを作成
root = tk.Tk()
root.title("URL Generator")

# ラベルとエントリボックスの作成
label_base_url = tk.Label(root, text="Base URL:")
label_base_url.pack()
entry_base_url = tk.Entry(root, width=50)
entry_base_url.pack()

label_path = tk.Label(root, text="Path:")
label_path.pack()
entry_path = tk.Entry(root, width=50)
entry_path.pack()

label_query = tk.Label(root, text="Query:")
label_query.pack()
entry_query = tk.Entry(root, width=50)
entry_query.pack()

# ボタンの作成
button_generate = tk.Button(root, text="Generate URL and Open Browser", command=on_generate_button_click)
button_generate.pack()

# Tkinterのメインループを開始
root.mainloop()