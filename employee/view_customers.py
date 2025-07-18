import tkinter as tk
from tkinter import ttk, messagebox
from db_config import get_connection
from assets import style

def view_customers():
    win = tk.Toplevel()
    win.title("View Customers")
    win.geometry("600x400")
    win.configure(bg=style.BG_COLOR)

    tk.Label(win, text="Customer List", font=style.TITLE_FONT, bg=style.BG_COLOR).pack(pady=10)

    tree = ttk.Treeview(win, columns=("Cust_ID", "Cust_name", "Mob_number"), show="headings")
    for col in tree["columns"]:
        tree.heading(col, text=col)
    tree.pack(pady=10, fill="both", expand=True)

    def refresh():
        for i in tree.get_children():
            tree.delete(i)
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT Cust_ID, Cust_name, Mob_number FROM CUSTOMER")
        for row in cursor.fetchall():
            tree.insert("", tk.END, values=row)
        conn.close()

    def delete():
        selected = tree.selection()
        if not selected:
            return
        item = tree.item(selected[0])
        cust_id = item['values'][0]

        conn = get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("DELETE FROM CUSTOMER WHERE Cust_ID = %s", (cust_id,))
            conn.commit()
            refresh()
        except Exception as e:
            messagebox.showerror("Error", str(e))
        finally:
            conn.close()

    def update():
        selected = tree.selection()
        if not selected:
            return
        item = tree.item(selected[0])
        old_data = item['values']

        upd_win = tk.Toplevel()
        upd_win.title("Update Customer")
        upd_win.geometry("300x250")
        upd_win.configure(bg=style.BG_COLOR)

        labels = ["Cust_name", "Mob_number"]
        entries = {}

        for i, label in enumerate(labels):
            tk.Label(upd_win, text=label, font=style.FONT, bg=style.BG_COLOR).grid(row=i, column=0, pady=10)
            entry = tk.Entry(upd_win, font=style.FONT)
            entry.insert(0, old_data[i+1])
            entry.grid(row=i, column=1)
            entries[label] = entry

        def submit_update():
            new_name = entries["Cust_name"].get()
            new_mob = entries["Mob_number"].get()
            conn = get_connection()
            cursor = conn.cursor()
            try:
                cursor.execute("UPDATE CUSTOMER SET Cust_name=%s, Mob_number=%s WHERE Cust_ID=%s",
                               (new_name, new_mob, old_data[0]))
                conn.commit()
                upd_win.destroy()
                refresh()
            except Exception as e:
                messagebox.showerror("Error", str(e))
            finally:
                conn.close()

        tk.Button(upd_win, text="Update", font=style.FONT, bg=style.BTN_COLOR, fg="white",
                command=submit_update).grid(row=3, columnspan=2, pady=20)

    btn_frame = tk.Frame(win, bg=style.BG_COLOR)
    btn_frame.pack(pady=10)

    tk.Button(btn_frame, text="Refresh", font=style.FONT, bg=style.BTN_COLOR, fg="white", command=refresh).grid(row=0, column=0, padx=5)
    tk.Button(btn_frame, text="Update", font=style.FONT, bg=style.BTN_COLOR, fg="white", command=update).grid(row=0, column=1, padx=5)
    tk.Button(btn_frame, text="Delete", font=style.FONT, bg=style.BTN_COLOR, fg="white", command=delete).grid(row=0, column=2, padx=5)

    refresh()