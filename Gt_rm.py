import tkinter as tk
from tkinter import ttk
def get_rom(room,root):
    #root.destroy()
    return room.get()
def find_room(room,ROOMs):
    lst=[]
    str_=''
    roms= open('rooms.txt','r')
    for x in roms.read():
        if room.get().lower() == x:
            lst.append(x)
    for x in lst:
        str_+=str(x)
        str_+='\n'
    ROOMs.set(str_)

def main():
    root = tk.Tk()
    room = tk.StringVar()
    ROOMs =tk.StringVar()
    root.geometry('300x300')
    root.resizable(False, False)
    root.title('GT RM')
    tk.Label(root, text='Room:').grid(row=0, column=0)
    tk.Entry(root,textvariable=room).grid(row=0, column=1)
    frame = tk.Frame(root,borderwidth=5,relief='flat')
    frame.grid(row=1, column=0)
    tk.Label(frame,textvariable=ROOMs).grid(row=0, column=0)
    tk.Button(root, text='Get Room', command=lambda:get_rom(room,root)).grid(row=0, column=2)
    tk.Button(root, text='Find Room', command=lambda:find_room(room,ROOMs)).grid(row=1, column=2)
    tk.Button(root, text='Exit', command=root.destroy).grid(row=2, column=2)
    root.mainloop()