import tkinter as tk
from tkinter import ttk
from db_config import get_connection
from assets import style

def view_beneficiaries(cust_id):
    win = tk.Toplevel()
    win.title("Beneficiaries")
    win.geometry("500x350")
    win.configure(bg=style.BG_COLOR)

    tk.Label(win, text="Your Beneficiaries", font=style.TITLE_FONT, bg=style.BG_COLOR).pack(pady=10)

    tree = ttk.Treeview(win, columns=("Beneficiary_ID", "Beneficiary_name", "Relationship"), show="headings")
    for col in tree["columns"]:
        tree.heading(col, text=col)
    tree.pack(pady=10, fill="x", expand=True)

    def load_beneficiaries():
        tree.delete(*tree.get_children())
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT Beneficiary_ID, Beneficiary_name, Relationship FROM BENEFICIARY WHERE Cust_ID = %s", (cust_id,))
        for row in cursor.fetchall():
            tree.insert("", tk.END, values=row)
        conn.close()

    load_beneficiaries()

    def open_add_form():
        form = tk.Toplevel()
        form.title("Add Beneficiary")
        form.geometry("300x250")
        form.configure(bg=style.BG_COLOR)

        tk.Label(form, text="Beneficiary Name:", font=style.FONT, bg=style.BG_COLOR).pack(pady=5)
        name_entry = tk.Entry(form, font=style.FONT)
        name_entry.pack()

        tk.Label(form, text="Relationship:", font=style.FONT, bg=style.BG_COLOR).pack(pady=5)
        relation_entry = tk.Entry(form, font=style.FONT)
        relation_entry.pack()

        msg = tk.Label(form, bg=style.BG_COLOR, font=style.FONT)
        msg.pack(pady=10)

        def submit():
            name = name_entry.get().strip()
            relation = relation_entry.get().strip()

            if not name or not relation:
                msg.config(text="Please fill all fields", fg="red")
                return

            try:
                conn = get_connection()
                cursor = conn.cursor()
                cursor.execute(
                    "INSERT INTO BENEFICIARY (Cust_ID, Beneficiary_name, Relationship) VALUES (%s, %s, %s)",
                    (cust_id, name, relation)
                )
                conn.commit()
                conn.close()
                msg.config(text="Beneficiary Added", fg="green")
                load_beneficiaries()
            except Exception as e:
                msg.config(text=f"Error: {e}", fg="red")

        tk.Button(form, text="Submit", font=style.FONT, bg=style.BTN_COLOR, fg="white", command=submit).pack(pady=10)

    tk.Button(win, text="Add Beneficiary", font=style.FONT, bg=style.BTN_COLOR, fg="white", command=open_add_form).pack(pady=20)
