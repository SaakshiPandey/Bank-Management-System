# 🏦 Bank Management System

A simple yet powerful Bank Management System built using **Python (Tkinter)** for the GUI and **MySQL** as the backend database. This application allows bank employees to manage customer and account information with ease.

---

## 🚀 Features

- 🔐 **Login System** for employees  
- 👤 **Customer Management**  
  - Add, update, delete customer details  
- 💳 **Account Management**  
  - View balance  
  - Deposit and withdraw money  
- 📁 **Database Integration**  
  - MySQL for persistent data storage  
- 🖼️ **GUI using Tkinter**  
  - Clean and user-friendly interface

---

## 🛠️ Technologies Used

- **Python 3.x**
- **Tkinter** – for building the GUI
- **MySQL** – for database management
- **SQLite** (optional/alternative db used in `.db` file)
- **SQL** – for creating and managing tables

---

## 📂 Project Structure

```
Bank-Management-System/
│
├── assets/                  # Images, icons, and other UI assets
├── customer/                # Customer-related interface and logic
├── employee/                # Employee login and dashboard
├── login/                   # Login interface
├── bank.sql                 # SQL script for database structure
├── bankdb.session.sql       # Additional session setup script
├── banking_mana.sql         # Sample bank management queries
├── banking_system.db        # SQLite database (optional)
├── db_config.py             # MySQL database configuration
├── main.py                  # Entry point of the application
├── LICENSE
├── README.md
└── .gitignore
```

---

## 🔧 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/SaakshiPandey/Bank-Management-System.git
cd Bank-Management-System
```

---

### 2. Set Up MySQL Database

- Open MySQL and create a new database.
- Run the `bank.sql` script to create the necessary tables:

```sql
SOURCE path/to/bank.sql;
```

- Update your MySQL credentials in `db_config.py`:

```python
host = "localhost"
user = "your_username"
password = "your_password"
database = "your_database_name"
```

---

### 3. Run the Application

Make sure your MySQL server is running.

```bash
python main.py
```

---

## ✅ Requirements

- Python 3.x  
- MySQL Server  
- `mysql-connector-python` (Install via: `pip install mysql-connector-python`)

---

## 📌 Notes

- SQLite version is included (`banking_system.db`) for easy testing without a MySQL server.  
- Basic error handling and validations are included.  
- Suitable for learning, college projects, or small-scale bank simulations.

---

## 📃 License

This project is licensed under the MIT License.  
See the `LICENSE` file for details.
