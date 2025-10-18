import tkinter as tk
from tkinter import ttk
import login
import requests
import Gt_rm
username = login.LogIN()[True]
room = Gt_rm.main()
print(room)
def post_message(message,username,room):
    requests.put(f'http://192.168.191.173:5000/main/{room}', data={'data': message,"username":username})


def get_messages(username,room):
    response =requests.get(f'http://192.168.191.173:5000/main/{room}',data={'username':username})
    #print(response.text)
    chats_window.delete('1.0',tk.END)
    chats_window.insert('1.0',requests.get(f'http://192.168.191.173:5000/main/{room}',data={'username':username}).text)
    chat_window.after(1000,lambda: get_messages(username,room))
chat_window = tk.Tk()
message=tk.StringVar()
messages=tk.StringVar()
chat_window.title('Chat')
chat_window.resizable(width=False, height=True)
chat_window.geometry('600x300')
user_label = tk.Label(chat_window,text=f'{username}:')
user_label.place(x=25,y=50)
username_entry = tk.Entry(chat_window, width=20,textvariable=message)
username_entry.place(x=100,y=50)
chat_frame = tk.Frame(chat_window,relief='raised',borderwidth=5)
chat_frame.place(x=50,y=100)
room_label = tk.Label(chat_frame,text=f'Room:{room}')
chats_window=tk.Text(chat_frame,width=50,height=20)
chats_window.pack(side='bottom')
#accesschat=tk.Button(chat_frame,text='Access Chat',command=lambda: get_messages(username,messages))
#accesschat.pack()
mesage_send=tk.Button(chat_window,text='Send',command=lambda: post_message(message.get(),username))
mesage_send.place(x=50,y=80)
get_messages(username,room)
chat_window.mainloop()
