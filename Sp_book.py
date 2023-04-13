import tkinter as tk



root = tk.Tk()
root.geometry("600x600")
root.resizable(False,False)
root.title("Special Occasion Booking")
root.configure(bg='light pink')

bg_image = tk.PhotoImage(file="m.png")
bg_label = tk.Label(root, image=bg_image)
bg_label.place(x=0, y=275)


def book_special_occasion():
    name = name_entry.get()
    email = email_entry.get()
    phone = phone_entry.get()
    date = date_entry.get()
    occasion_type = occasion_type_entry.get()

    success_label = tk.Label(root, text="Booking for " + occasion_type + " on " + date + " successful! Our Reception will reach you for more details.", fg="green")
    success_label.pack()

name_label = tk.Label(root, text="Name:")
name_label.pack()
name_entry = tk.Entry(root)
name_entry.pack()

email_label = tk.Label(root, text="Email:")
email_label.pack()
email_entry = tk.Entry(root)
email_entry.pack()

phone_label = tk.Label(root, text="Phone:")
phone_label.pack()
phone_entry = tk.Entry(root)
phone_entry.pack()

date_label = tk.Label(root, text="Date (YYYY-MM-DD):")
date_label.pack()
date_entry = tk.Entry(root)
date_entry.pack()

occasion_type_label = tk.Label(root, text="Type of Occasion:")
occasion_type_label.pack()
occasion_type_entry = tk.Entry(root)
occasion_type_entry.pack()

book_button = tk.Button(root, text="Book Now", command=book_special_occasion)
book_button.pack()

root.mainloop()
