import tkinter as tk
from tkinter import *

class yh():
    def __init__(self, master):
        self.master = master
        self.bottom = Frame(master, height=150, bg='white')
        self.bottom.pack(fill=X)
        self.top = Frame(master, height=400, bg='white')
        self.top.pack(fill=X)

        self.heading = Label(self.bottom, text='My tele diary', bg='white', fg='#004c8b', font= 'Arial 19 bold')
        self.heading.place(x=340, y=25)

        self.contactsbutton = Button(text=' View Contacts', font='Arial 15 bold')
        self.contactsbutton.place(x=339, y=375)
        self.addbutton = Button(text='Add Contact', font='Arial 15 bold')
        self.addbutton.place(x=350, y=325)


def epic():
    global win
    win = Tk()
    diary = yh(win)
    win.title('Telephone Diary ting')
    win.geometry('825x550')


if __name__ == '__main__':
    epic()


win.mainloop()