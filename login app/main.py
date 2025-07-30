from tkinter import*

root = Tk()
root.title('login app')
root.geometry('400x500')

frame = Frame(master=root,height=250,width=400,bg='white')

lbl1 = Label(frame,text="Full Name", bg='black',fg='white',width=12)
lbl2 = Label(frame,text="Email ID", bg='black',fg='white',width=12)
lbl3 = Label(frame,text="Enter Password", bg='black',fg='white',width=12)

name_entry = Entry(frame)
mail_entry = Entry(frame)
pass_entry = Entry(frame, show='*')
  
def display():
    name = name_entry.get()
    greet = "Hey "+ name
    message = "\nCongratulation on your account"
    textbox.insert(END,greet)
    textbox.insert(END, message)

textbox = Text(bg='cyan',fg='white',height=230,width=350)


btn = Button(text="Create", command=display,bg='red')

frame.place(x=0,y=0)
lbl1.place(x=20,y=40)
name_entry.place(x=150,y=40)
lbl2.place(x=20,y=100)
mail_entry.place(x=150,y=100)
lbl3.place(x=20,y=150)
pass_entry.place(x=150,y=150)
btn.place(x=100,y=180)
textbox.place(x=20,y=300)

root.mainloop()
