import tkinter as tk
from login.customer_login import CustomerLogin
from login.employee_login import EmployeeLogin
from assets import style
import mysql.connector  # MySQL connector

# Function to connect to MySQL database
def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="saakshi",
        database="banking_system"  # Your MySQL database
    )

# Create Account window
def create_account_window():
    def create_account():
        name = name_entry.get().strip()
        mobile = mobile_entry.get().strip()

        if name and mobile.isdigit():
            try:
                conn = connect_db()
                cursor = conn.cursor()

                cursor.execute("INSERT INTO CUSTOMER (Cust_name, Mob_number) VALUES (%s, %s)", (name, mobile))
                conn.commit()

                cursor.execute("SELECT LAST_INSERT_ID()")
                customer_id = cursor.fetchone()[0]

                message_label.config(text=f"Account Created! Customer ID: {customer_id}", fg="green")

                conn.close()
            except Exception as e:
                message_label.config(text=f"Database Error: {str(e)}", fg="red")
        else:
            message_label.config(text="Enter valid name and numeric mobile number.", fg="red")

    # New window for account creation
    account_window = tk.Toplevel()
    account_window.title("Create Account")
    account_window.geometry("400x350")
    account_window.configure(bg=style.BG_COLOR)

    tk.Label(account_window, text="Enter Name and Mobile", font=style.FONT, bg=style.BG_COLOR).pack(pady=20)

    tk.Label(account_window, text="Name", bg=style.BG_COLOR, font=style.FONT).pack()
    name_entry = tk.Entry(account_window, font=style.FONT)
    name_entry.pack(pady=10)

    tk.Label(account_window, text="Mobile Number", bg=style.BG_COLOR, font=style.FONT).pack()
    mobile_entry = tk.Entry(account_window, font=style.FONT)
    mobile_entry.pack(pady=10)

    tk.Button(account_window, text="Create Account", bg=style.BTN_COLOR, fg="white", font=style.FONT, command=create_account).pack(pady=15)

    message_label = tk.Label(account_window, text="", bg=style.BG_COLOR, font=style.FONT)
    message_label.pack(pady=10)

# Main welcome screen
def home_screen():
    root = tk.Tk()
    root.title("Banking System")
    root.geometry("400x300")
    root.configure(bg=style.BG_COLOR)

    tk.Label(root, text="Welcome to Bank System", font=style.TITLE_FONT, bg=style.BG_COLOR).pack(pady=30)

    tk.Button(root, text="Customer Login", bg=style.BTN_COLOR, fg="white", font=style.FONT,
            command=lambda: [root.destroy(), CustomerLogin()]).pack(pady=10)

    tk.Button(root, text="Employee Login", bg=style.BTN_COLOR, fg="white", font=style.FONT,
            command=lambda: [root.destroy(), EmployeeLogin()]).pack(pady=10)

    tk.Button(root, text="Create Account", bg=style.BTN_COLOR, fg="white", font=style.FONT,
            command=create_account_window).pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    home_screen()
