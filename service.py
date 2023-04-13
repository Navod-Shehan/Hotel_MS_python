import tkinter as tk
from tkinter import *
from tkinter import PhotoImage
from tkinter import messagebox
import os

def reserve():
    root.destroy()
    os.system('python reserve.py')

def contact():
    root.destroy()
    os.system('python contact.py')

def occasion():
    root.destroy()
    os.system('python Sp_book.py')



root = tk.Tk()
root.geometry("1200x1000")
root.resizable(False,False)
root.configure(bg='light blue')
root.title('Services')

heading=Label(root,text='Welcome to Our Hotel . We are looking forward to providing you with great service! ',fg="#000000",bg="White" ,font=("Gill Sans MT", 20))
heading.place(x=35,y=25)

image = PhotoImage(file="3.png")

button1 = Button(root, text="Sign Up",image=image,font=("Arial", 20),command=reserve)
button1.configure(width=250, height=250)
button1.place(x=70, y=150)

image2 = PhotoImage(file="Update your reservation.png")

button1 = Button(root,image=image2,font=("Arial", 20))
button1.configure(width=250, height=250)
button1.place(x=480, y=150)



image3 = PhotoImage(file="sp.png")

button1 = Button(root,image=image3,font=("Arial", 20),command=occasion)
button1.configure(width=250, height=250)
button1.place(x=480+410, y=150)

image4 = PhotoImage(file="4.png")

button1 = Button(root,image=image4,font=("Arial", 20),command=contact)
button1.configure(width=250, height=250)
button1.place(x=480, y=500)

root.mainloop()