# login/customer_login.py
import tkinter as tk
from tkinter import messagebox
from db_config import get_connection
from customer.dashboard import CustomerDashboard
from assets import style

def CustomerLogin():
    root = tk.Tk()
    root.title("Customer Login")
    root.geometry("300x200")
    root.configure(bg=style.BG_COLOR)

    tk.Label(root, text="Enter Customer ID", bg=style.BG_COLOR, font=style.FONT).pack(pady=10)
    cust_id_entry = tk.Entry(root, font=style.FONT)
    cust_id_entry.pack()

    def login():
        cid = cust_id_entry.get()
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM CUSTOMER WHERE Cust_ID = %s", (cid,))
        result = cursor.fetchone()
        conn.close()

        if result:
            root.destroy()
            CustomerDashboard(cid)
        else:
            messagebox.showerror("Login Failed", "Invalid Customer ID")

    tk.Button(root, text="Login", bg=style.BTN_COLOR, fg="white", font=style.FONT, command=login).pack(pady=20)

    root.mainloop()
