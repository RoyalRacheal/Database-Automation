import pymysql
from pymysql import cursors

connection = pymysql.connect(
    host = "localhost",
    user = "root",
    password = "",
    db = "banking",
    charset = "utf8mb4",
    cursorclass = pymysql.cursors.DictCursor
)

###Creating Customer_info table
def create_table1():
    with connection.cursor() as cursor:     
        add_table_customer = """                     
            CREATE TABLE IF NOT EXISTS customer_info(
                customer_id INT(10) AUTO_INCREMENT NOT NULL PRIMARY KEY,
                full_name VARCHAR(20),
                gender VARCHAR(6),
                state_of_residence VARCHAR(10),
                Date_of_birth DATE
                
            );
        """
        cursor.execute(add_table_customer)
        connection.commit()


###Creating Account_info table
def create_table2():
    with connection.cursor() as cursor:     
        add_table_account = """                     
            CREATE TABLE IF NOT EXISTS Account_info(
                account_id INT(10) AUTO_INCREMENT NOT NULL PRIMARY KEY,
                customer_id INT(10) NOT NULL, 
                FOREIGN KEY Account_info(customer_id) REFERENCES customer_info(customer_id),
                account_number BIGINT(11) UNIQUE,
                account_pin INT(4),
                account_balance FLOAT(15, 2) 
                
            );
        """
        cursor.execute(add_table_account)
        connection.commit()

###Creating Transaction_info table
def create_table3():
    with connection.cursor() as cursor:     
        add_table_transaction = """                     
            CREATE TABLE IF NOT EXISTS Transaction_info(
                Transaction_id INT(10) AUTO_INCREMENT NOT NULL PRIMARY KEY,
                customer_id INT(10) NOT NULL, 
                FOREIGN KEY Transaction_info(customer_id) REFERENCES customer_info(customer_id),
                transaction_type CHAR(6),
                amount FLOAT(15, 2),
                D_O_T DATETIME NOT NULL                
            );
        """
        cursor.execute(add_table_transaction)
        connection.commit()


### Filling the Customer_info Table
def write_dataC(current_name, current_gender, current_str, current_DOB):
    with connection.cursor() as cursor:
        add_record = f"""
            INSERT INTO customer_info(full_name, gender, state_of_residence, Date_of_birth)
            VALUES
            ('{current_name}', '{current_gender}', '{current_str}', {current_DOB});

        """

        cursor.execute(add_record)
        connection.commit()


### Filling the Account_info Table
def write_data(current_acc_no, current_acc_pin, current_acc_bal):
    with connection.cursor() as cursor:
        add_record = f"""
            INSERT INTO account_info (account_number, account_pin, account_balance)
            VALUES
            ({current_acc_no}, {current_acc_pin}, {current_acc_bal});

        """

        cursor.execute(add_record)
        connection.commit()

###Writing into Transaction table
def write_dataT(current_transc_type, current_amount, current_status, current_DOT):
    with connection.cursor() as cursor:
        add_record = f"""
            INSERT INTO Transaction_info (transaction_type, amount, status, D_O_T)
            VALUES
            ('{current_transc_type}', {current_amount}, '{current_status}', {current_DOT});

        """

        cursor.execute(add_record)

        connection.commit()

##UPDATNG ACCOUNT BALANCES
def update_account(current_custid, current_acc_bal):
    with connection.cursor() as cursor:
        update_data = f"UPDATE account_info SET account_balance = {current_acc_bal} WHERE customer_id = {current_custid};"
        cursor.execute(update_data)
        connection.commit()


create_table1()
create_table2()
create_table3()
