# import tkinter as tk



# root = tk.Tk()
# root.geometry("600x600")
# root.resizable(False,False)
# root.title("Special Occasion Booking")
# root.configure(bg='light pink')

# bg_image = tk.PhotoImage(file="m.png")
# bg_label = tk.Label(root, image=bg_image)
# bg_label.place(x=0, y=275)


# def book_special_occasion():
#     name = name_entry.get()
#     email = email_entry.get()
#     phone = phone_entry.get()
#     date = date_entry.get()
#     occasion_type = occasion_type_entry.get()

#     success_label = tk.Label(root, text="Booking for " + occasion_type + " on " + date + " successful! Our Reception will reach you for more details.", fg="green")
#     success_label.pack()

# name_label = tk.Label(root, text="Name:")
# name_label.pack()
# name_entry = tk.Entry(root)
# name_entry.pack()

# email_label = tk.Label(root, text="Email:")
# email_label.pack()
# email_entry = tk.Entry(root)
# email_entry.pack()

# phone_label = tk.Label(root, text="Phone:")
# phone_label.pack()
# phone_entry = tk.Entry(root)
# phone_entry.pack()

# date_label = tk.Label(root, text="Date (YYYY-MM-DD):")
# date_label.pack()
# date_entry = tk.Entry(root)
# date_entry.pack()

# occasion_type_label = tk.Label(root, text="Type of Occasion:")
# occasion_type_label.pack()
# occasion_type_entry = tk.Entry(root)
# occasion_type_entry.pack()

# book_button = tk.Button(root, text="Book Now", command=book_special_occasion)
# book_button.pack()

# root.mainloop()



import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import os

def book_special_occasion():
    name = entry_name.get()
    email = entry_email.get()
    phone = entry_phone.get()
    date = entry_date.get()
    occasion_type = entry_type.get()

    success_label = tk.Label(root, text="Booking for " + occasion_type + " on " + date + " successful! Our Reception will reach you for more details.", fg="green")
    success_label.pack()



# Create a main window
root = tk.Tk()
root.title("Special booking")
root.geometry("700x500")

# Load the background image
image = Image.open("m.png")
image = image.resize((700, 500))
photo = ImageTk.PhotoImage(image)

# Create a canvas widget
canvas = tk.Canvas(root, width=700, height=500)
canvas.pack()

# Add the background image to the canvas
canvas.create_image(0, 0, anchor=tk.NW, image=photo)

# Create the sign-up form
label0 = Label(text="Special Occasion Booking", font=("Arial Bold", 18),bg="#593a76",fg="white")
label0.place(relx=0.5, rely=0.11, anchor=CENTER)

label_name = tk.Label(root, text="Name :", bg="#1e4e75", fg="white", font=(5))
label_name.place(x=170, y=100)
entry_name = tk.Entry(root,bg="#1e4e75",font=(5))
entry_name.place(x=250, y=100)

label_email = tk.Label(root, text="Email :",bg="#1e4e75", fg="white", font=(5))
label_email.place(x=173, y=150)
entry_email = tk.Entry(root,bg="#1e4e75", font=(5))
entry_email.place(x=250, y=150)

label_phone = tk.Label(root, text="Phone :",bg="#1e4e75", fg="white", font=(5))
label_phone.place(x=167, y=200)
entry_phone = tk.Entry(root,bg="#1e4e75", font=(5))
entry_phone.place(x=250, y=200)

label_date = tk.Label(root, text="Date :",bg="#1e4e75", fg="white", font=(5))
label_date.place(x=180, y=250)
entry_date = tk.Entry(root,bg="#1e4e75", font=(5))
entry_date.place(x=250, y=250)
entry_date.insert(0, 'YYYY-MM-DD')
entry_date.bind("<FocusIn>", lambda event: entry_date.delete(0, "end"))

label_type = tk.Label(root, text="Type of Occasion:",bg="#1e4e75", fg="white", font=(5))
label_type.place(x=73, y=300)
entry_type = tk.Entry(root,bg="#1e4e75", font=(5))
entry_type.place(x=250, y=300)

button = tk.Button(root, text="Book Now", bg="#1e4e75", fg="white", font=("Helvetica", 12),command=book_special_occasion)

button.place(relx=0.5, rely=0.75, anchor=tk.CENTER)

# Start the main loop
root.mainloop()
