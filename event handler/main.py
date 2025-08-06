from  tkinter import*

root = Tk()
root.title('Event Handler')
root.geometry('400x400')

def handle_keypress(event):
    print(event.char)

root.bind("<Key>", handle_keypress)

def handle_click(event):
    print("\nThe button was clicked")

btn = Button(text="click me!")
btn.pack()

btn.bind("<Button-1>", handle_click)
root.mainloop()