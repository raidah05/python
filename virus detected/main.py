from tkinter import*
from tkinter import messagebox
root = Tk()
root.geometry('300x300')

def msg():
    messagebox.showwarning("Alert!", "Stop! Virus Found")

btn = Button(root, text="Scan for virus", command=msg)
btn.place(x=40,y=80)

root.mainloop()