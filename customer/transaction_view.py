import tkinter as tk
from tkinter import ttk
from db_config import get_connection
from assets import style
from datetime import datetime

def view_transactions(cust_id):
    win = tk.Toplevel()
    win.title("Transactions")
    win.geometry("600x400")
    win.configure(bg=style.BG_COLOR)

    tk.Label(win, text="Your Transactions", font=style.TITLE_FONT, bg=style.BG_COLOR).pack(pady=10)

    # Transaction table
    tree = ttk.Treeview(win, columns=("trans_ID", "trans_date", "amount"), show="headings")
    tree.heading("trans_ID", text="ID")
    tree.heading("trans_date", text="Date")
    tree.heading("amount", text="Amount")
    tree.pack(pady=10, fill="both", expand=True)

    # Function to load transactions from DB
    def load_transactions():
        tree.delete(*tree.get_children())
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT trans_ID, trans_date, amount FROM TRANSACTION WHERE Cust_ID = %s", (cust_id,))
        for row in cursor.fetchall():
            tree.insert("", tk.END, values=row)
        conn.close()

    load_transactions()

    # Function to open a new transaction form
    def open_transaction_form():
        form = tk.Toplevel()
        form.title("New Transaction")
        form.geometry("300x250")
        form.configure(bg=style.BG_COLOR)

        tk.Label(form, text="Amount:", font=style.FONT, bg=style.BG_COLOR).pack(pady=5)
        amount_entry = tk.Entry(form, font=style.FONT)
        amount_entry.pack()

        msg_label = tk.Label(form, bg=style.BG_COLOR, font=style.FONT)
        msg_label.pack(pady=10)

        def submit_transaction():
            amount = amount_entry.get()
            if not amount:
                msg_label.config(text="Amount cannot be empty", fg="red")
                return

            try:
                conn = get_connection()
                cursor = conn.cursor()
                cursor.execute(
                    "INSERT INTO TRANSACTION (Cust_ID, trans_date, amount) VALUES (%s, %s, %s)",
                    (cust_id, datetime.now(), float(amount))
                )
                conn.commit()
                conn.close()
                msg_label.config(text="Transaction Added", fg="green")
                load_transactions()
            except Exception as e:
                msg_label.config(text=f"Error: {e}", fg="red")

        tk.Button(form, text="Submit", font=style.FONT, bg=style.BTN_COLOR, fg="white", command=submit_transaction).pack(pady=10)

    # Button to make new transaction
    tk.Button(win, text="Make Transaction", font=style.FONT, bg=style.BTN_COLOR, fg="white", command=open_transaction_form).pack(pady=20)

