# app_ui.py
import tkinter as tk
from file_generator import generate_txt

def on_generate_button_click():
    email = email_entry.get()
    incoming_server = incoming_server_entry.get()
    incoming_account = incoming_account_entry.get()
    incoming_password = incoming_password_entry.get()
    outgoing_server = outgoing_server_entry.get()
    outgoing_account = outgoing_account_entry.get()
    outgoing_password = outgoing_password_entry.get()
    
    generate_txt(email, incoming_server, incoming_account, incoming_password, outgoing_server, outgoing_account, outgoing_password)

app = tk.Tk()
app.title("TXT Generator")

tk.Label(app, text="Email").grid(row=0, column=0, padx=10, pady=5)
email_entry = tk.Entry(app)
email_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(app, text="Incoming Server").grid(row=1, column=0, padx=10, pady=5)
incoming_server_entry = tk.Entry(app)
incoming_server_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Label(app, text="Incoming Account Name").grid(row=2, column=0, padx=10, pady=5)
incoming_account_entry = tk.Entry(app)
incoming_account_entry.grid(row=2, column=1, padx=10, pady=5)

tk.Label(app, text="Incoming Password").grid(row=3, column=0, padx=10, pady=5)
incoming_password_entry = tk.Entry(app, show="*")
incoming_password_entry.grid(row=3, column=1, padx=10, pady=5)

tk.Label(app, text="Outgoing Server").grid(row=4, column=0, padx=10, pady=5)
outgoing_server_entry = tk.Entry(app)
outgoing_server_entry.grid(row=4, column=1, padx=10, pady=5)

tk.Label(app, text="Outgoing Account Name").grid(row=5, column=0, padx=10, pady=5)
outgoing_account_entry = tk.Entry(app)
outgoing_account_entry.grid(row=5, column=1, padx=10, pady=5)

tk.Label(app, text="Outgoing Password").grid(row=6, column=0, padx=10, pady=5)
outgoing_password_entry = tk.Entry(app, show="*")
outgoing_password_entry.grid(row=6, column=1, padx=10, pady=5)

generate_button = tk.Button(app, text="Generate TXT", command=on_generate_button_click)
generate_button.grid(row=7, column=0, columnspan=2, pady=10)

app.mainloop()