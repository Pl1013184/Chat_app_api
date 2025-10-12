import tkinter as tk
import login
import requests
username = login.LogIN()[True]
def post_message(message):
    requests.post('http://127.0.0.1:5000/main/chat', data={'data': message})
chat_window = tk.Tk()
message=tk.StringVar()
chat_window.title('Chat')
chat_window.resizable(width=False, height=False)
chat_window.geometry('600x150')
user_label = tk.Label(chat_window,text=f'{username}:')
user_label.place(x=25,y=50)
username_entry = tk.Entry(chat_window, width=20,textvariable=message)
username_entry.place(x=50,y=50)
mesage_send=tk.Button(chat_window,text='Send',command=lambda: post_message(message.get()))
mesage_send.place(x=50,y=80)
chat_window.mainloop()