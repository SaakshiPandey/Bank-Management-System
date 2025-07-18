import tkinter as tk
from . import add_customer, view_customers

from assets import style

def EmployeeDashboard(emp_name):
    root = tk.Tk()
    root.title("Employee Dashboard")
    root.geometry("400x300")
    root.configure(bg=style.BG_COLOR)

    # Updated to show employee's name instead of ID
    tk.Label(root, text=f"Welcome", font=style.TITLE_FONT, bg=style.BG_COLOR).pack(pady=20)

    tk.Button(root, text="Add Customer", font=style.FONT, bg=style.BTN_COLOR, fg="white",
              command=add_customer.AddCustomerForm).pack(pady=10)

    tk.Button(root, text="View / Edit Customers", font=style.FONT, bg=style.BTN_COLOR, fg="white",
              command=view_customers.view_customers).pack(pady=10)

    root.mainloop()
