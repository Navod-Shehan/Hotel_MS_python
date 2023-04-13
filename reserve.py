from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import datetime
import os

root = Tk()
root.geometry('650x650')
root.title("Reservation")
reserve_label = Label(text="Room Booking", font=("Arial", 20))

reserve_label.pack()
reserve_label.place(x=240, y=80)
# root.configure(bg='light green')
# root.title('Services')

# Create Frame
frame1 = Frame(root, relief=RIDGE, padx=10, pady=10)
frame1.pack(fill=BOTH, expand=True)
frame1.place(x=100, y=150)

# Create Labels
lbl_arrival = Label(frame1, text="Arrival Date(Y-M-D)", font=("Arial Bold", 12))
lbl_arrival.grid(row=0, column=0, padx=10, pady=10)

lbl_departure = Label(frame1, text="Departure Date (Y-M-D)", font=("Arial Bold", 12))
lbl_departure.grid(row=1, column=0, padx=10, pady=10)

lbl_rooms = Label(frame1, text="Number of Rooms", font=("Arial Bold", 12))
lbl_rooms.grid(row=2, column=0, padx=10, pady=10)

lbl_people = Label(frame1, text="Number of People", font=("Arial Bold", 12))
lbl_people.grid(row=3, column=0, padx=10, pady=10)

lbl_roomtype = Label(frame1, text="Room Type", font=("Arial Bold", 12))
lbl_roomtype.grid(row=4, column=0, padx=10, pady=10)

lbl_food = Label(frame1, text="Do you need Food from hotel?", font=("Arial Bold", 12))
lbl_food.grid(row=5, column=0, padx=10, pady=10)

cal_arrival = Entry(frame1, width=12)
cal_arrival.grid(row=0, column=1)

cal_departure = Entry(frame1, width=12)
cal_departure.grid(row=1, column=1)

cmb_rooms = ttk.Combobox(frame1, width=10, state='readonly',
                         values=('1', '2', '3', '4','5','6','7','8','9','10'))
cmb_rooms.current(0)
cmb_rooms.grid(row=2, column=1)

cmb_people = ttk.Combobox(frame1, width=10, state='readonly',
                          values=('1', '2', '3', '4', '5', '6','7','8','9','10'))
cmb_people.current(0)
cmb_people.grid(row=3, column=1)

cmb_roomtype = ttk.Combobox(frame1, width=20, state='readonly',
                            values=('Deluxe', 'Luxury', 'Standard'))
cmb_roomtype.current(0)
cmb_roomtype.grid(row=4, column=1)

chk_food = Checkbutton(frame1, text="Yes")
chk_food.grid(row=5, column=1)
chk_food = Checkbutton(frame1, text="No")
chk_food.grid(row=5, column=3)

def calculate_price():
    price = 0
    arrival_date = datetime.datetime.strptime(cal_arrival.get(), "%Y-%m-%d").date()
    departure_date = datetime.datetime.strptime(cal_departure.get(), "%Y-%m-%d").date()
    days = (departure_date - arrival_date).days
    rooms = int(cmb_rooms.get())
    if cmb_roomtype.get() == 'Deluxe':
        price = 100
    elif cmb_roomtype.get() == 'Luxury':
        price = 200
    elif cmb_roomtype.get() == 'Standard':
        price = 50
    total_price = price * rooms * days

    food_var = BooleanVar()
    chk_food = Checkbutton(root, text="Include Food", variable=food_var)
    chk_food.pack()

    if food_var.get():
        print("Food included!")
        total_price += 100
        messagebox.showinfo("Total Price", f"Total Price: ${total_price}")

    else:
        print("No food.")
        payment_method = messagebox.askquestion("Payment Method", f"The total price is {total_price:.2f} USD. Would you like to pay by card?")

    if payment_method == 'yes':
            root.destroy()
            os.system("python pay.py")
    else:
        messagebox.showinfo("Message","Pay your bill to the reception")



create_bill= Button(root, text="Calculate Bill", font=("Arial", 20),background="#4CAF50", foreground="black", command=calculate_price)
create_bill.pack()
create_bill.place(x=250, y=450)


root.mainloop()
