import tkinter
from tkinter import *
from tkinter import PhotoImage
import os

def sign_in():
    root.destroy()
    os.system('python sign_in.py')


def signup():
    root.destroy()
    os.system('python signup.py')

root = Tk()
root.geometry("900x950")
root.resizable(False,False)


canvas = Canvas(root, width=600, height=950)
canvas.pack(side=RIGHT)

image = PhotoImage(file="booking_03.png")

resized_image = image.subsample(6)

canvas.create_image(0, 0, image=resized_image, anchor=NW)


login_button = Button(root, text="Sign In",height= 1, width=6, font=("Arial", 12), bg='white',activebackground='light blue', command=sign_in)
login_button.pack(pady=50)
login_button.place(x=800, y=20)

signup_button = Button(root, text="Sign Up",height= 1, width=6, font=("Arial", 12), bg='white', command=signup)
signup_button.pack(pady=20)
signup_button.place(x=700, y=20)


welcome_label = Label(root, text="WELCOME\n to \nOcean Hotel ", font=("DynaPuff", 32),anchor='w')
welcome_label.place(x=25, y=150)
text_box = Label(root, width=29, height=12, text="We offer \n luxurious and comfortable\n stay with top-notch amenities. \n\n Our rooms are \n elegantly designed with \n modern\n furnishings and beautiful views.\n\nCome and experience \n the ultimate relaxation\n and hospitality." , font=("Calibri", 14))
text_box.place(x=0,y=400)



root.mainloop()
