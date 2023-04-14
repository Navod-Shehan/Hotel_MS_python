from tkinter import *
from tkinter import messagebox
import os


def service():
    os.system('python service.py')

def signin():
    root.destroy()
    os.system('python entering.py')

def check_credentials():
    username = username_entry.get()
    password = password_entry.get()

    if username == "user" and password == "123":
        messagebox.showinfo("Success", "Login successful!")
        root.destroy()
        os.system("python service.py")

    else:messagebox.showerror("Error", "Invalid username or password.")

# root=Tk()
# root.title('Login')
# root.geometry('700x700')
# root.resizable(False,False)

# canvas = Canvas(root, width=800, height=800)
# canvas.pack()
# img = PhotoImage(file="m_2388719.png")

# canvas.create_image(0, 0, anchor=NW, image=img)

# label0 = Label(canvas, text="Login Portal", bg="red", font=("Arial Bold", 18))
# label0.place(relx=0.5, rely=0.1, anchor=CENTER)


# username_label = Label(canvas, text="Username:", bg="white", font=("Arial", 14))
# username_label.place(relx=0.5, rely=0.3, anchor=CENTER)

# username_entry = Entry(canvas, font=("Arial", 14))
# username_entry.place(relx=0.5, rely=0.4, anchor=CENTER)

# password_label = Label(canvas, text="Password:", bg="white", font=("Arial", 14))
# password_label.place(relx=0.5, rely=0.5, anchor=CENTER)

# password_entry = Entry(canvas, show="*", font=("Arial", 14))
# password_entry.place(relx=0.5, rely=0.6, anchor=CENTER)

# login_button = Button(canvas, text="Sign In", bg="white", font=("Arial", 13),command=check_credentials)
# login_button.place(relx=0.5, rely=0.7, anchor=CENTER)

# status_label = Label(canvas, text="", bg="white", font=("Arial", 14))
# status_label.place(relx=0.5, rely=0.8, anchor=CENTER)


# B1 = Button(root, text="Back", bg="green", fg="white", width=8,command=service)
# B1.place(x=0, y=0, anchor="nw")

# root.mainloop()

import tkinter as tk
from PIL import Image, ImageTk

# Create the main window
root = tk.Tk()
root.title("Login")
root.geometry("500x300")
root.resizable(False, False)

# Load an image
image = Image.open("login_1.jpg")
image = image.resize((500, 300))
photo = ImageTk.PhotoImage(image)

# Create a label to display the image
image_label = tk.Label(root, image=photo)
image_label.place(x=0, y=0, relwidth=1, relheight=1)

# Create the widgets
label0 = Label(text="Login Portal", font=("Arial Bold", 18),bg="#11182a",fg="white")
# label0.place(relx=0.5, rely=0.1, anchor=CENTER)
label1 = tk.Label(root, text="Username", font=("Helvetica", 12), fg="white", bg="#11182a")
entry1 = tk.Entry(root, font=("Helvetica", 12),background="#435777")
label2 = tk.Label(root, text="Password", font=("Helvetica", 12), fg="white", bg="#11182a")
entry2 = tk.Entry(root, show="*", font=("Helvetica", 12),background="#435777")
button = tk.Button(root, text="Login", bg="#11182a", fg="white", font=("Helvetica", 12),command=check_credentials)
button_back = tk.Button(root, text="Back", bg="#11182a", fg="red", font=("Helvetica", 12),command=service)

# Add the widgets to the window
label0.place(relx=0.25, rely=0.2, anchor=CENTER)
label1.place(relx=0.25, rely=0.4, anchor=tk.CENTER)
entry1.place(relx=0.25, rely=0.5, anchor=tk.CENTER)
label2.place(relx=0.25, rely=0.6, anchor=tk.CENTER)
entry2.place(relx=0.25, rely=0.7, anchor=tk.CENTER)
button.place(relx=0.25, rely=0.9, anchor=tk.CENTER)
button_back.place(relx=0.05, rely=0.05, anchor=tk.CENTER)

# Start the main loop
root.mainloop()
