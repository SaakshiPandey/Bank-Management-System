-- Create Tables
CREATE TABLE DEPARTMENT (
    Dept_ID INT AUTO_INCREMENT PRIMARY KEY,
    Dept_name VARCHAR(50)
);

CREATE TABLE BRANCH (
    Branch_ID INT AUTO_INCREMENT PRIMARY KEY,banking_system
    Branch_name VARCHAR(50),
    location VARCHAR(100),
    Dept_ID INT,
    FOREIGN KEY (Dept_ID) REFERENCES DEPARTMENT(Dept_ID)
);

CREATE TABLE EMPLOYEE (
    Emp_ID INT AUTO_INCREMENT PRIMARY KEY,
    Emp_name VARCHAR(50),
    position VARCHAR(50),
    Branch_ID INT,
    Dept_ID INT,
    FOREIGN KEY (Branch_ID) REFERENCES BRANCH(Branch_ID),
    FOREIGN KEY (Dept_ID) REFERENCES DEPARTMENT(Dept_ID)
);

CREATE TABLE CUSTOMER (
    Cust_ID INT AUTO_INCREMENT PRIMARY KEY,
    Cust_name VARCHAR(50),
    Mob_number VARCHAR(15)
);

CREATE TABLE ACCOUNT (
    Acc_ID INT AUTO_INCREMENT PRIMARY KEY,
    Cust_ID INT,
    Acc_type VARCHAR(20),
    balance DECIMAL(10,2),
    FOREIGN KEY (Cust_ID) REFERENCES CUSTOMER(Cust_ID)
);

CREATE TABLE CARD (
    Card_ID INT AUTO_INCREMENT PRIMARY KEY,
    Cust_ID INT,
    Card_type VARCHAR(20),
    Expiry_date DATE,
    FOREIGN KEY (Cust_ID) REFERENCES CUSTOMER(Cust_ID)
);

CREATE TABLE LOCKER (
    Locker_ID INT AUTO_INCREMENT PRIMARY KEY,
    Cust_ID INT,
    Locker_type VARCHAR(20),
    location VARCHAR(100),
    FOREIGN KEY (Cust_ID) REFERENCES CUSTOMER(Cust_ID)
);

CREATE TABLE LOAN (
    Loan_ID INT AUTO_INCREMENT PRIMARY KEY,
    Cust_ID INT,
    Loan_type VARCHAR(50),
    interest DECIMAL(5,2),
    FOREIGN KEY (Cust_ID) REFERENCES CUSTOMER(Cust_ID)
);

CREATE TABLE BENEFICIARY (
    Beneficiary_ID INT AUTO_INCREMENT PRIMARY KEY,
    Cust_ID INT,
    Beneficiary_name VARCHAR(50),
    Relationship VARCHAR(30),
    FOREIGN KEY (Cust_ID) REFERENCES CUSTOMER(Cust_ID)
);

CREATE TABLE TRANSACTION (
    trans_ID INT AUTO_INCREMENT PRIMARY KEY,
    Cust_ID INT,
    trans_date DATE,
    amount DECIMAL(10,2),
    FOREIGN KEY (Cust_ID) REFERENCES CUSTOMER(Cust_ID)
);

-- ✅ Trigger to update account balance after transaction
DELIMITER $$

CREATE TRIGGER update_balance_after_transaction
AFTER INSERT ON TRANSACTION
FOR EACH ROW
BEGIN
    UPDATE ACCOUNT
    SET balance = balance - NEW.amount
    WHERE Cust_ID = NEW.Cust_ID;
END$$

DELIMITER ;

-- ✅ Stored Procedure with Cursor to show customer loans
DELIMITER $$

CREATE PROCEDURE ShowCustomerLoans()
BEGIN
    DECLARE done INT DEFAULT FALSE;
    DECLARE cid INT;
    DECLARE cname VARCHAR(50);
    DECLARE ltype VARCHAR(50);
    DECLARE lrate DECIMAL(5,2);
    
    DECLARE loan_cursor CURSOR FOR
        SELECT CUSTOMER.Cust_ID, CUSTOMER.Cust_name, LOAN.Loan_type, LOAN.interest
        FROM CUSTOMER
        JOIN LOAN ON CUSTOMER.Cust_ID = LOAN.Cust_ID;

    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;

    OPEN loan_cursor;

    read_loop: LOOP
        FETCH loan_cursor INTO cid, cname, ltype, lrate;
        IF done THEN
            LEAVE read_loop;
        END IF;
        -- Show loan info (you can also insert this into an audit table)
        SELECT CONCAT('Customer ID: ', cid, ', Name: ', cname, ', Loan: ', ltype, ', Interest: ', lrate) AS Loan_Info;
    END LOOP;

    CLOSE loan_cursor;
END$$

DELIMITER ;

-- ✅ To execute the stored procedure
-- CALL ShowCustomerLoans();
