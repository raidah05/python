from tkinter import*

root= Tk()
root.title('Number pad')
root.geometry('250x300')

num = [[9,8,7],[6,5,4],[3,2,1],['#',0,'*']]

for i in range(4):
    root.columnconfigure(i , weight=1, minsize=50)
    root.rowconfigure(i,weight=1, minsize=50)

for i in range(4):
    for j in range(3):
        frame = Frame(
            master = root,
            relief=SUNKEN,
            borderwidth=1,
            bg='black'
        )
        frame.grid(row=i,column=j, sticky='nsew')
        label = Label(master=frame, text=num[i][j], bg= 'white', font=('Arial', 18))
        label.pack(expand=True, fill='both',padx=5,pady=1)

root.mainloop()