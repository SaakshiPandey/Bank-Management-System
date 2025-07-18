import tkinter as tk
from tkinter import ttk
from db_config import get_connection
from assets import style

def view_loans(cust_id):
    win = tk.Toplevel()
    win.title("Loans")
    win.geometry("500x350")
    win.configure(bg=style.BG_COLOR)

    tk.Label(win, text="Your Loans", font=style.TITLE_FONT, bg=style.BG_COLOR).pack(pady=10)

    # Loan table
    tree = ttk.Treeview(win, columns=("Loan_ID", "Loan_type", "interest"), show="headings")
    tree.heading("Loan_ID", text="Loan ID")
    tree.heading("Loan_type", text="Loan Type")
    tree.heading("interest", text="Interest")
    tree.pack(pady=10, fill="x", expand=True)

    # Function to load loans from DB
    def load_loans():
        tree.delete(*tree.get_children())
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT Loan_ID, Loan_type, interest FROM LOAN WHERE Cust_ID = %s", (cust_id,))
        for row in cursor.fetchall():
            tree.insert("", tk.END, values=row)
        conn.close()

    load_loans()

    # Function to open the loan application form
    def open_apply_form():
        form = tk.Toplevel()
        form.title("Apply for Loan")
        form.geometry("300x250")
        form.configure(bg=style.BG_COLOR)

        tk.Label(form, text="Loan Type:", font=style.FONT, bg=style.BG_COLOR).pack(pady=5)
        type_entry = tk.Entry(form, font=style.FONT)
        type_entry.pack()

        tk.Label(form, text="Interest Rate (%):", font=style.FONT, bg=style.BG_COLOR).pack(pady=5)
        interest_entry = tk.Entry(form, font=style.FONT)
        interest_entry.pack()

        msg = tk.Label(form, font=style.FONT, bg=style.BG_COLOR)
        msg.pack(pady=10)

        def apply():
            loan_type = type_entry.get().strip()
            interest = interest_entry.get().strip()

            if not loan_type or not interest:
                msg.config(text="Please fill all fields", fg="red")
                return

            try:
                interest_float = float(interest)
            except ValueError:
                msg.config(text="Interest must be a number", fg="red")
                return

            try:
                conn = get_connection()
                cursor = conn.cursor()
                cursor.execute(
                    "INSERT INTO LOAN (Cust_ID, Loan_type, interest) VALUES (%s, %s, %s)",
                    (cust_id, loan_type, interest_float)
                )
                conn.commit()
                conn.close()
                msg.config(text="Loan Application Submitted", fg="green")
                load_loans()
            except Exception as e:
                msg.config(text=f"Error: {e}", fg="red")

        tk.Button(form, text="Submit", font=style.FONT, bg=style.BTN_COLOR, fg="white", command=apply).pack(pady=10)

    # Button to apply for a new loan
    tk.Button(win, text="Apply for Loan", font=style.FONT, bg=style.BTN_COLOR, fg="white", command=open_apply_form).pack(pady=20)

