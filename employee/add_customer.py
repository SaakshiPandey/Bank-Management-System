import tkinter as tk
from tkinter import messagebox
from db_config import get_connection
from assets import style

def AddCustomerForm():
    win = tk.Toplevel()
    win.title("Add Customer")
    win.geometry("400x400")
    win.configure(bg=style.BG_COLOR)

    labels = ["Cust_ID", "Cust_name", "Mob_number"]
    entries = {}

    for i, label in enumerate(labels):
        tk.Label(win, text=label, font=style.FONT, bg=style.BG_COLOR).grid(row=i, column=0, pady=10, padx=10)
        entry = tk.Entry(win, font=style.FONT)
        entry.grid(row=i, column=1)
        entries[label] = entry

    def save():
        values = tuple(entries[label].get() for label in labels)
        if any(not v for v in values):
            messagebox.showerror("Error", "All fields are required")
            return

        conn = get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO CUSTOMER (Cust_ID, Cust_name, Mob_number) VALUES (%s, %s, %s)", values)
            conn.commit()
            messagebox.showinfo("Success", "Customer added successfully")
            win.destroy()
        except Exception as e:
            messagebox.showerror("Error", str(e))
        finally:
            conn.close()

    tk.Button(win, text="Submit", font=style.FONT, bg=style.BTN_COLOR, fg="white", command=save).grid(row=len(labels), columnspan=2, pady=20)

