import tkinter as tk
from tkinter import ttk
from db_config import get_connection
from assets import style

def view_cards(cust_id):
    win = tk.Toplevel()
    win.title("Cards")
    win.geometry("500x300")  # Increased width for better spacing
    win.configure(bg=style.BG_COLOR)

    tk.Label(win, text="Your Cards", font=style.TITLE_FONT, bg=style.BG_COLOR).pack(pady=10)

    # Treeview with the proper columns: Card Number, Card Type, and Expiry Date
    tree = ttk.Treeview(win, columns=("CardNumber", "CardType", "Expiry_date"), show="headings")
    tree.heading("CardNumber", text="Card Number")
    tree.heading("CardType", text="Card Type")
    tree.heading("Expiry_date", text="Expiry Date")
    tree.pack(pady=10, fill="x")

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT Card_ID, Card_type, Expiry_date FROM CARD WHERE Cust_ID = %s", (cust_id,))
    for row in cursor.fetchall():
        tree.insert("", tk.END, values=row)
    conn.close()
