import tkinter as tk
from tkinter import ttk
def get_rom(room):
    print(room.get())
    return room.get()
def main():
    root = tk.Tk()
    room = tk.StringVar()
    root.geometry('300x300')
    root.resizable(width=0, height=0)
    root.title('GT RM')
    tk.Label(root, text='Room:').grid(row=0, column=0)
    tk.Entry(root,textvariable=room).grid(row=0, column=1)
    tk.Button(root, text='Get Room', command=lambda:get_rom(room)).grid(row=0, column=2)
    root.mainloop()
#main()