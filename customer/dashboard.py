# customer/dashboard.py
import tkinter as tk
from customer import account_view, card_view, loan_view, locker_view, transaction_view, beneficiary_view
from assets import style

def CustomerDashboard(cust_id):
    root = tk.Tk()
    root.title("Customer Dashboard")
    root.geometry("400x400")
    root.configure(bg=style.BG_COLOR)

    tk.Label(root, text=f"Welcome Customer {cust_id}", font=style.TITLE_FONT, bg=style.BG_COLOR).pack(pady=20)

    buttons = [
        ("View Accounts", account_view.view_accounts),
        ("View Cards", card_view.view_cards),
        ("View Loans", loan_view.view_loans),
        ("View Lockers", locker_view.view_lockers),
        ("View Transactions", transaction_view.view_transactions),
        ("View Beneficiaries", beneficiary_view.view_beneficiaries),
    ]

    for text, command in buttons:
        tk.Button(root, text=text, font=style.FONT, bg=style.BTN_COLOR, fg="white",
                command=lambda cmd=command: cmd(cust_id)).pack(pady=5)

    root.mainloop()
