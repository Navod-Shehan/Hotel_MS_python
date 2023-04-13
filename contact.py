# from tkinter import *
# from tkinter import messagebox
# from tkinter import PhotoImage
# import os


# def back():
#     root.destroy()
#     os.system('python service.py')

# root=Tk()
# root.title('Reach to us')

# root.geometry('1280x800')
# root.configure(bg="#fff")
# root.resizable(False,False)
# img=PhotoImage(file="contact window image.png")
# Label(root,image=img,bg='white').place(x=100,y=0)


# bbutton = Button(root, text="Back", command=back, width=20 )
# bbutton.pack(pady=20)
# bbutton.place(x=5, y=5)




# root.mainloop()


import tkinter as tk
import os
from PIL import ImageTk, Image

class ContactUsGUI:
    def __init__(self, master):
        self.master = master
        master.title("Contact Us")

        # Create a label for the page title
        # self.page_title = tk.Label(master, text="Contact Us", font=("Helvetica", 24))
        # self.page_title.pack(pady=20)

        # Load the image and resize it
        self.image = Image.open("contact_1.png")
        self.image = self.image.resize((800, 200), Image.ANTIALIAS)

        # Convert the image to Tkinter format
        self.image_tk = ImageTk.PhotoImage(self.image)

        # Create a label for the image
        self.image_label = tk.Label(master, image=self.image_tk)
        self.image_label.pack()

        # Create a frame for the form fields
        self.form_frame = tk.Frame(master)
        self.form_frame.pack(pady=20)

        # Create a label for the name field
        self.name_label = tk.Label(self.form_frame, text="Name:", font=("Helvetica", 12))
        self.name_label.grid(row=0, column=0, pady=10)

        # Create an entry field for the name
        self.name_entry = tk.Entry(self.form_frame, font=("Helvetica", 12), width=30)
        self.name_entry.grid(row=0, column=1, pady=10)

        # Create a label for the email field
        self.email_label = tk.Label(self.form_frame, text="Email:", font=("Helvetica", 12))
        self.email_label.grid(row=1, column=0, pady=10)

        # Create an entry field for the email
        self.email_entry = tk.Entry(self.form_frame, font=("Helvetica", 12), width=30)
        self.email_entry.grid(row=1, column=1, pady=10)

        # Create a label for the message field
        self.message_label = tk.Label(self.form_frame, text="Message:", font=("Helvetica", 12))
        self.message_label.grid(row=2, column=0, pady=10)

        # Create a text field for the message
        self.message_text = tk.Text(self.form_frame, font=("Helvetica", 12), height=10, width=30)
        self.message_text.grid(row=2, column=1, pady=10)

        # Create a button to submit the form
        self.submit_button_1 = tk.Button(master, text="Back", font=("Helvetica", 14), command=self.back)
        self.submit_button_1.pack(pady=20)
        self.submit_button_1.place(x=320, y=530)

        self.submit_button_2 = tk.Button(master, text="Submit", font=("Helvetica", 14), command=self.submit_form)
        self.submit_button_2.pack(pady=20)
        self.submit_button_2.place(x=470, y=530)

    def submit_form(self):
        name = self.name_entry.get()
        email = self.email_entry.get()
        message = self.message_text.get("1.0", "end-1c")

        # Here, you would do something with the form data (e.g. send an email)

        # Clear the form fields
        self.name_entry.delete(0, "end")
        self.email_entry.delete(0, "end")
        self.message_text.delete("1.0", "end")

    def back(self):
        root.destroy()
        os.system('python service.py')

root = tk.Tk()
contact_us_gui = ContactUsGUI(root)
root.geometry('800x700')
root.mainloop()
