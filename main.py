from tkinter import *
from tkinter import messagebox
from tkinter import PhotoImage
import os


def enter():
    root.destroy()
    os.system('python entering.py')

root=Tk()
root.title('Home')
root.geometry('1280x720')
root.configure(bg="#fff")
root.resizable(False,False)
img2=PhotoImage(file="Untitled design.png")
Label(root,image=img2,bg='white').place(x=0,y=0)

welcome_label = Label(root, text="Login as ",fg="white", font=("DynaPuff", 14),anchor='w')
welcome_label.config(bg='#192968')
welcome_label.place(x=950, y=60)

# text_box = Label(root, text="Login as " , font=("Calibri", 14))
# text_box.place(x=950, y=60)

signup_button = Button(root, text="Customer", font=("Arial", 12), bg='#f6bc00', command=enter)
# signup_button.pack(pady=20)
signup_button.place(x=1050, y=60)

signup_button = Button(root, text="Admin", font=("Arial", 12), bg='#f6bc00')
# signup_button.pack(pady=20)
signup_button.place(x=1150, y=60)


root.mainloop()