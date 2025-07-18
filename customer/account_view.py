import tkinter as tk
from tkinter import ttk
from db_config import get_connection
from assets import style

def view_accounts(cust_id):
    win = tk.Toplevel()
    win.title("Accounts")
    win.geometry("500x300")  # Increased width for balance column
    win.configure(bg=style.BG_COLOR)

    tk.Label(win, text="Your Accounts", font=style.TITLE_FONT, bg=style.BG_COLOR).pack(pady=10)

    # Treeview with an additional column for balance
    tree = ttk.Treeview(win, columns=("Acc_ID", "Acc_type", "Balance"), show="headings")
    tree.heading("Acc_ID", text="Account ID")
    tree.heading("Acc_type", text="Type")
    tree.heading("Balance", text="Balance")
    tree.pack(pady=10, fill="x")

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT Acc_ID, Acc_type, balance FROM ACCOUNT WHERE Cust_ID = %s", (cust_id,))
    for row in cursor.fetchall():
        tree.insert("", tk.END, values=row)
    conn.close()
