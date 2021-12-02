from Mini_Project_Functions import *
import random as rd
from datetime import datetime as dt



class Bankreq:
    def __init__(self, What_to_do, full_name, gender, State_of_residence, D_O_B):
        self.full_name = full_name
        self.gender = gender
        self.State_of_residence = State_of_residence
        self.D_O_B = D_O_B
        self.account_no = rd.randrange(1000000000, 1999999999)
        self.account_bal = 0
        self.account_pin = 0     

    def get_full_name(self):
        return self.full_name

    def get_account_no(self):
        return self.account_no

    def get_account_pin(self):
        return self.account_pin

    def get_gender(self):
        return self.gender

    def get_State_of_residence(self):
        return self.State_of_residence

    def get_D_O_B(self):
        return self.D_O_B

    def get_check_balance(self):
        return f"Your account balance is: {self.account_bal}"

    def deposit(self, value):
        self.account_bal += value
        write_dataT(self.current_customer_id, "Credit", value, "Successful", dt.now())
        update_account(self.current_customer_id, current_acc_bal)
        
        print("Transaction Sucessful!")

    def withdrawal(self, value):
        if self.account_bal >= value:
            self.account_bal -= value
            write_dataT(self.current_customer_id, "Dedit", value, "Successful", dt.now())
            update_account(self.current_customer_id, current_acc_bal)
            print("Transaction Successful!")
        else:
            print("Insufficient Funds!")


print("Welcome to Royal Diadem Bank...\n")
What_to_do = int(input("What would you like to do? Enter 1 to Sign up, enter 2 to login: "))
if What_to_do == 1:
    ask_full_name = input("Enter your full name here: ")
    ask_gender = input("Enter gender here: ")
    ask_state_resd = input("Enter your State of Residence here: ")
    ask_D_O_B = input("Enter your Date of birth in YYYY-MM-DD format here: ")

    customer_info = Bankreq(ask_full_name, ask_gender, ask_state_resd, ask_D_O_B)
    print(f"Welcome {customer_info.get_full_name()},\n")
    print(f"Your account number is {customer_info.get_account_no()} \n")

    current_name = customer_info.get_full_name
    current_gender = customer_info.get_gender
    current_str = customer_info.get_State_of_residence
    current_DOB = ask_D_O_B
    current_acc_no = customer_info.get_account_no
    current_acc_pin = customer_info.get_account_pin
    current_acc_bal = customer_info.get_check_balance
    write_dataC(current_name, current_gender, current_str, current_DOB)
    

    def account_pin():
        while True:
            ask_account_pin = int(input("Select a four digit pin here: "))
            ask_account_pin_again = int(input("Enter your four digit pin here again: "))
            if ask_account_pin == ask_account_pin_again:
                print("Pin set successfully! \n")
                break
            else:
                print("Your pins didn't match, please try again\n")
            
    account_pin()

    ###Getting the customer id of the latest customer
    with connection.cursor() as cursor:
        customer_details = "SELECT customer_id FROM customer_info;"
        cursor.execute(customer_details)
        connection.commit()
        result = cursor.fetchall()
        current_customer_id = result[-1]["customer_id"]

    
## Login
elif What_to_do == 2:
    with connection.cursor() as cursor:
        my_query = "SELECT customer_id, account_no, account_pin FROM account_info;"
        cursor.execute(my_query)
        connection.commit()
        result = cursor.fetchall()
    
        while True:
            ask_acc_no = int(input("Enter your account number here: "))
            ask_acc_pin = int(input("Enter your 4 digits pin here: "))
            for entry in result:
                if (entry["account_number"] == ask_acc_no) and (entry["account_pin"] == ask_acc_pin):
                    print("Login Successful")
                    break  
            else:
                print("Incorrect details...")

        ##Fetching Customer details from the database
    with connection.cursor() as cursor:
        query_customer = f"SELECT customer_info.full_name, customer_info.gender, customer_info.state_of_residence, customer_info.Date_of_birth, account_info.account_no, account_info.account_bal, account_info.account_pin FROM customer_info INNER JOIN account_info ON customer_info.customer_id = account_info.customer_id WHERE customer_info.customer_id = {self.current_customer_id};"
        cursor.execute(query_customer)
        connection.commit()
        customer_details = cursor.fetchall()
        current_name = customer_details[0]["full_name"]
        current_gender = customer_details[0]["gender"]
        current_str = customer_details[0]["state_of_residence"]
        current_DOB = customer_details[0]["date_of_birth"]
        current_acc_bal = customer_details[0]["account_balance"]
        current_acc_no = customer_details[0]["account_number"]
        current_acc_pin = customer_details[0]["account_pin"]
       
else:
    pass



def menu():
    while True:
        print("\n")
        print("Enter 1 to access acount balance\nEnter 2 to make deposits\nEnter 3 to make withdrawal\nEnter 9 to quit")
        ask = int(input("Enter option here: "))
        if ask == 1:
            print(f"\n Your account balance is {customer_info.get_check_balance()}")
        elif ask == 2:
            further = int(input("Enter amount here: "))
            customer_info.deposit(further)
        elif ask == 3:
            further = int(input("Enter amount here: "))
            customer_info.withdrawal(further)
        elif ask == 9:
            print("Thank you for banking with us!")
            break
        else:
            pass
        
menu()


