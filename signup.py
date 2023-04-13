from tkinter import *
from tkinter import messagebox
import os


root=Tk()
root.title('Sign up')
root.geometry('800x800')
root.configure(bg="#fff")
root.resizable(False,False)
img=PhotoImage(file="m_2396608 (3).png")
Label(root,image=img,bg='White').place(x=0,y=0)


def signin():
    root.destroy()
    os.system('python entering.py')

B1 = Button(root, text="Back", bg="green", fg="white", width=8,command=signin)
B1.place(x=0, y=0, anchor="nw")


frame=Frame(root,width=500, height=500,bg="pink")
frame.place(x=90,y=70)

name_label = Label(frame, text='Name:' ,font=("calibri Bold ", 18),bg=('pink') ,fg=('green'))
name_label.grid(row=0, column=0)
name_entry = Entry(frame,width=30)
name_entry.grid(row=0, column=1)

email_label = Label(frame, text='Email:',font=("calibri Bold ", 18), bg=('pink') ,fg=('green'))
email_label.grid(row=1, column=0)
email_entry = Entry(frame,width=30)
email_entry.grid(row=1, column=1)

password_label = Label(frame, text='Password:',font=("calibri Bold", 18),bg=('pink') , fg=('green'))
password_label.grid(row=2, column=0)
password_entry = Entry(frame, width=30,show='*')
password_entry.grid(row=2, column=1)

confirm_password_label = Label(frame, text='Confirm Password:',font=("calibri Bold ", 18),bg=('pink') , fg=('green'))
confirm_password_label.grid(row=3, column=0)
confirm_password_entry = Entry(frame ,width=30,show='*')
confirm_password_entry.grid(row=3, column=1)


def sign_up():
    messagebox.showinfo("Sign Up Successful", "Your account has been created!")


button = Button(root, width=15, height=3,text="Sign Up Now",bg="DarkBlue",fg="White",border=0,font=("Microsoft Tai Le Bold",17), highlightthickness=0,command=sign_up)
button.place(x=550, y=80)



root.mainloop()
