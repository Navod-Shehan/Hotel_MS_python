import tkinter as tk
from tkinter import messagebox
from tkinter import ttk



class PaymentPage(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        # Create style for button
        style = ttk.Style()
        style.configure("Custom.TButton", font=("Arial", 16), background = "#4CAF50", foreground = "black", borderwidth=0, padding=10)

        # Create widgets
        self.payment_label = tk.Label(self, text="Payment Page", font=("Arial", 20))
        self.card_number_label = tk.Label(self, text="Card Number:", font=("Arial", 14))
        self.card_number_entry = tk.Entry(self, font=("Arial", 14))
        self.expiry_date_label = tk.Label(self, text="Expiry Date:", font=("Arial", 14))
        self.expiry_date_entry = tk.Entry(self, font=("Arial", 14))
        self.cvv_label = tk.Label(self, text="CVV:", font=("Arial", 14))
        self.cvv_entry = tk.Entry(self, font=("Arial", 14))
        self.pay_button = ttk.Button(self, text="Pay", style="Custom.TButton", command=self.pay)

        # Layout widgets
        self.payment_label.pack(pady=20)
        self.card_number_label.pack()
        self.card_number_entry.pack(pady=10)
        self.expiry_date_label.pack()
        self.expiry_date_entry.pack(pady=10)
        self.cvv_label.pack()
        self.cvv_entry.pack(pady=10)
        self.pay_button.pack(pady=20)

        # Allow frame to resize to fit contents
        self.pack_propagate(0)

    def pay(self):
        # Process payment
        messagebox.showinfo("Success", "Payement succses.Enjoy your stay !")
        root.destroy()

# Create main window
root = tk.Tk()
root.geometry("400x400")
root.title('Payement Portal')

# Create payment page
payment_page = PaymentPage(root)
payment_page.pack(expand=True, fill=tk.BOTH)

# Start GUI
root.mainloop()
        

