# outlook_draft_creator.py
import tkinter as tk
from tkinter import messagebox
import win32com.client

def create_outlook_draft(email, incoming_server, incoming_account, incoming_password, outgoing_server, outgoing_account, outgoing_password):
    if not (email and incoming_server and incoming_account and incoming_password and outgoing_server and outgoing_account and outgoing_password):
        messagebox.showerror("Error", "All fields must be filled out.")
        return

    content = (
        f"Email: {email}\n"
        f"Incoming Server: {incoming_server}\n"
        f"Incoming Account Name: {incoming_account}\n"
        f"Incoming Password: {incoming_password}\n"
        f"Outgoing Server: {outgoing_server}\n"
        f"Outgoing Account Name: {outgoing_account}\n"
        f"Outgoing Password: {outgoing_password}\n"
    )

    outlook = win32com.client.Dispatch("Outlook.Application")
    mail = outlook.CreateItem(0)
    mail.Subject = "Account Information"
    mail.Body = content
    mail.Save()
    messagebox.showinfo("Success", "Outlook draft created successfully!")