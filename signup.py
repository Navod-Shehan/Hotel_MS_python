# from tkinter import *
# from tkinter import messagebox
# import os


# root=Tk()
# root.title('Sign up')
# root.geometry('800x800')
# root.configure(bg="#fff")
# root.resizable(False,False)
# img=PhotoImage(file="m_2396608 (3).png")
# Label(root,image=img,bg='White').place(x=0,y=0)


# def signin():
#     root.destroy()
#     os.system('python entering.py')

# B1 = Button(root, text="Back", bg="green", fg="white", width=8,command=signin)
# B1.place(x=0, y=0, anchor="nw")


# frame=Frame(root,width=500, height=500,bg="pink")
# frame.place(x=90,y=70)

# name_label = Label(frame, text='Name:' ,font=("calibri Bold ", 18),bg=('pink') ,fg=('green'))
# name_label.grid(row=0, column=0)
# name_entry = Entry(frame,width=30)
# name_entry.grid(row=0, column=1)

# email_label = Label(frame, text='Email:',font=("calibri Bold ", 18), bg=('pink') ,fg=('green'))
# email_label.grid(row=1, column=0)
# email_entry = Entry(frame,width=30)
# email_entry.grid(row=1, column=1)

# password_label = Label(frame, text='Password:',font=("calibri Bold", 18),bg=('pink') , fg=('green'))
# password_label.grid(row=2, column=0)
# password_entry = Entry(frame, width=30,show='*')
# password_entry.grid(row=2, column=1)

# confirm_password_label = Label(frame, text='Confirm Password:',font=("calibri Bold ", 18),bg=('pink') , fg=('green'))
# confirm_password_label.grid(row=3, column=0)
# confirm_password_entry = Entry(frame ,width=30,show='*')
# confirm_password_entry.grid(row=3, column=1)


# def sign_up():
#     messagebox.showinfo("Sign Up Successful", "Your account has been created!")


# button = Button(root, width=15, height=3,text="Sign Up Now",bg="DarkBlue",fg="White",border=0,font=("Microsoft Tai Le Bold",17), highlightthickness=0,command=sign_up)
# button.place(x=550, y=80)



# root.mainloop()


import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import os


def sign_up():
    messagebox.showinfo("Sign Up Successful", "Your account has been created!")

def signin():
    root.destroy()
    os.system('python sign_in.py')

# Create a main window
root = tk.Tk()
root.title("Sign Up Page")
root.geometry("600x400")

# Load the background image
image = Image.open("signup_1.jpg")
image = image.resize((600, 400))
photo = ImageTk.PhotoImage(image)

# Create a canvas widget
canvas = tk.Canvas(root, width=600, height=400)
canvas.pack()

# Add the background image to the canvas
canvas.create_image(0, 0, anchor=tk.NW, image=photo)

# Create the sign-up form
label0 = Label(text="Sign Up", font=("Arial Bold", 18),bg="#1e4e75",fg="#041014")
label0.place(relx=0.5, rely=0.11, anchor=CENTER)

label_name = tk.Label(root, text="Name :", bg="#1e4e75", fg="white", font=(5))
label_name.place(x=170, y=100)
entry_name = tk.Entry(root,bg="#1e4e75",font=(5))
entry_name.place(x=250, y=100)

label_email = tk.Label(root, text="Email :",bg="#1e4e75", fg="white", font=(5))
label_email.place(x=173, y=150)
entry_email = tk.Entry(root,bg="#1e4e75", font=(5))
entry_email.place(x=250, y=150)

label_password = tk.Label(root, text="Password :",bg="#1e4e75", fg="white", font=(5))
label_password.place(x=132, y=200)
entry_password = tk.Entry(root, show="*",bg="#1e4e75", font=(5))
entry_password.place(x=250, y=200)

label_confirm = tk.Label(root, text="Confirm Password :",bg="#1e4e75", fg="white", font=(5))
label_confirm.place(x=60, y=250)
entry_confirm = tk.Entry(root, show="*",bg="#1e4e75", font=(5))
entry_confirm.place(x=250, y=250)

button = tk.Button(root, text="Sign Up", bg="#1e4e75", fg="white", font=("Helvetica", 12),command=sign_up)
button_back = tk.Button(root, text="Login", bg="#1e4e75", fg="#041014", font=("Helvetica", 12),command=signin)

button.place(relx=0.7, rely=0.84, anchor=tk.CENTER)
button_back.place(relx=0.5, rely=0.84, anchor=tk.CENTER)

# Start the main loop
root.mainloop()
