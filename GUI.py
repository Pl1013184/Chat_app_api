import tkinter as tk
from tkinter import ttk
import login
import requests
import Gt_rm
#username = login.LogIN()[True]
#Gt_rm.main()
username= 'admin'
with open('file.txt', 'r') as f:
    room=f.read()
with open('file.txt','w') as f:
    f.write('')
room='test'
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


chat_frame = tk.Frame(chat_window,relief='raised',borderwidth=5)
chat_frame.pack()
room_label = tk.Label(chat_frame,text=f'Room:{room}')
room_label.grid(row=0,column=0)
chats_window=tk.Text(chat_frame,width=75,height=15)
chats_window.grid(row=1,column=0)
#accesschat=tk.Button(chat_frame,text='Access Chat',command=lambda: get_messages(username,messages))
#accesschat.pack()
entry_frame= tk.Frame(chat_frame,relief='raised',borderwidth=5)
entry_frame.grid(row=2,column=0)
user_label = tk.Label(entry_frame,text=f'{username}:')
user_label.grid(row=0,column=0)
username_entry = tk.Entry(entry_frame, width=20,textvariable=message)
username_entry.grid(row=0,column=1)
mesage_send=tk.Button(entry_frame,text='Send',command=lambda: post_message(message.get(),username,room))
mesage_send.grid(row=0,column=2)
get_messages(username,room)
chat_window.mainloop()
