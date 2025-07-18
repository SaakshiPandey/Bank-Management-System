import tkinter as tk
from tkinter import messagebox
from db_config import get_connection
from employee.dashboard import EmployeeDashboard
from assets import style

def EmployeeLogin():
    root = tk.Tk()
    root.title("Employee Login")
    root.geometry("300x200")
    root.configure(bg=style.BG_COLOR)

    tk.Label(root, text="Enter Employee ID", bg=style.BG_COLOR, font=style.FONT).pack(pady=10)
    emp_id_entry = tk.Entry(root, font=style.FONT)
    emp_id_entry.pack()

    def login():
        eid = emp_id_entry.get()
        conn = get_connection()
        if conn is None:
            messagebox.showerror("Error", "Database connection failed")
            return
        cursor = conn.cursor()
        cursor.execute("SELECT Emp_ID FROM EMPLOYEE WHERE Emp_ID = %s", (eid,))
        result = cursor.fetchone()
        conn.close()

        if result:
            root.destroy()
            EmployeeDashboard(eid)
        else:
            messagebox.showerror("Login Failed", "Invalid Employee ID")

    tk.Button(root, text="Login", bg=style.BTN_COLOR, fg="white", font=style.FONT, command=login).pack(pady=20)

    root.mainloop()
