import tkinter as tk
from tkinter import ttk
from db_config import get_connection
from assets import style

def view_lockers(cust_id):
    win = tk.Toplevel()
    win.title("Lockers")
    win.geometry("450x350")
    win.configure(bg=style.BG_COLOR)

    tk.Label(win, text="Your Lockers", font=style.TITLE_FONT, bg=style.BG_COLOR).pack(pady=10)

    # Treeview to display lockers
    tree = ttk.Treeview(win, columns=("Locker ID", "Locker Type", "Location"), show="headings")
    tree.heading("Locker ID", text="Locker ID")
    tree.heading("Locker Type", text="Locker Type")
    tree.heading("Location", text="Location")
    tree.pack(pady=10, fill="x", expand=True)

    # Load lockers from DB
    def load_lockers():
        tree.delete(*tree.get_children())
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT Locker_ID, Locker_type, location FROM LOCKER WHERE Cust_ID = %s", (cust_id,))
        for row in cursor.fetchall():
            tree.insert("", tk.END, values=row)
        conn.close()

    load_lockers()

    # Form to avail locker
    def avail_locker():
        form = tk.Toplevel()
        form.title("Avail Locker")
        form.geometry("350x250")
        form.configure(bg=style.BG_COLOR)

        tk.Label(form, text="Locker Type (Small/Medium/Large):", font=style.FONT, bg=style.BG_COLOR).pack(pady=10)
        type_entry = tk.Entry(form, font=style.FONT)
        type_entry.pack()

        tk.Label(form, text="Location:", font=style.FONT, bg=style.BG_COLOR).pack(pady=10)
        location_entry = tk.Entry(form, font=style.FONT)
        location_entry.pack()

        msg = tk.Label(form, bg=style.BG_COLOR, font=style.FONT)
        msg.pack(pady=10)

        def submit():
            locker_type = type_entry.get().strip().capitalize()
            location = location_entry.get().strip()

            if locker_type not in ["Small", "Medium", "Large"]:
                msg.config(text="Enter valid locker type!", fg="red")
                return
            if not location:
                msg.config(text="Please enter location", fg="red")
                return

            try:
                conn = get_connection()
                cursor = conn.cursor()
                cursor.execute("INSERT INTO LOCKER (Cust_ID, Locker_type, location) VALUES (%s, %s, %s)", 
                               (cust_id, locker_type, location))
                conn.commit()
                conn.close()
                msg.config(text="Locker availed successfully!", fg="green")
                load_lockers()
            except Exception as e:
                msg.config(text=f"Error: {e}", fg="red")

        tk.Button(form, text="Submit", font=style.FONT, bg=style.BTN_COLOR, fg="white", command=submit).pack(pady=10)

    # Button to avail new locker
    tk.Button(win, text="Avail Locker", font=style.FONT, bg=style.BTN_COLOR, fg="white", command=avail_locker).pack(pady=20)
