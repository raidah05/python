from tkinter import*
from datetime import date

root = Tk()
root.title('getting started with widgets')
root.geometry('400x300')

lbl = Label(text="Hey There!" , fg="white", bg="navy blue", height=1 , width=300)
name_lbl = Label(text="Full name", bg="black",fg="white")
name_enter = Entry()

def display():
    name = name_enter.get()
    global message
    message = "Welcome to codingal! \n Today's date is :"

    greet = "Hello "+name+"\n"

    text_box.insert(END, greet)
    text_box.insert(END, message)
    text_box.insert(END, date.today())

    
text_box = Text(height=10)
butn = Button(text="Begin", height=1, command=display, bg="navy blue",fg="white")


lbl.pack()
name_lbl.pack()
name_enter.pack()
butn.pack()
text_box.pack()

root.mainloop()
