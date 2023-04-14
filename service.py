import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image

# Create the main window
root = tk.Tk()
root.title("Stylish Dashboard")

# Load an image
img1 = Image.open("3.png")
img1 = img1.resize((200, 200))
img1 = ImageTk.PhotoImage(img1)

img2 = Image.open("Update your reservation.png")
img2 = img2.resize((200, 200))
img2 = ImageTk.PhotoImage(img2)

img3 = Image.open("sp.png")
img3 = img3.resize((200, 200))
img3 = ImageTk.PhotoImage(img3)

img4 = Image.open("4.png")
img4 = img4.resize((200, 200))
img4 = ImageTk.PhotoImage(img4)

img5 = Image.open("contact_1.png")
img5 = img5.resize((1400, 330))
img5 = ImageTk.PhotoImage(img5)

# Define a custom style for the buttons
style = ttk.Style()
style.configure("Custom.TButton", font=("Courier", 14), foreground="#ffffff", background="#6c7ae0", padding=10, width=15)

# Create the widgets
label = ttk.Label(root, text="WELCOME TO OCEAN HOTEL !")
label.config(font=("Courier", 30), padding=10)
image1 = Image.open("contact_1.png")
image_label = ttk.Label(root, image=img5)
label1 = ttk.Label(root, text="We are looking forward to providing you with great service")
label1.config(font=("Courier", 30), padding=10)
button1 = ttk.Button(root, text="Button 1",image=img1, style="Custom.TButton")
button2 = ttk.Button(root, text="Button 2",image=img2, style="Custom.TButton")
button3 = ttk.Button(root, text="Button 3",image=img3, style="Custom.TButton")
button4 = ttk.Button(root, text="Button 4",image=img4, style="Custom.TButton")

label.grid(row=0, column=0, columnspan=4, pady=10)
image_label.grid(row=1, column=0, columnspan=4, pady=10)
label1.grid(row=2, column=0, columnspan=4, pady=10)
button1.grid(row=3, column=0, padx=10, pady=10)
button2.grid(row=3, column=1, padx=10, pady=10)
button3.grid(row=3, column=2, padx=10, pady=10)
button4.grid(row=3, column=3, padx=10, pady=10)

# Start the main loop
root.mainloop()
