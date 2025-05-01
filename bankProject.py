# Project Title: Simple Bank Management System
import pandas as pd
# step 1 : Account Creation
# Store customer details (Account Number, Name, Age, Account Type, Balance) in a list of tuples.
# Ensure each account number is unique.

accounts = [
    {"Account Number": 1001, "Name": "Amit Sharma", "Age": 32, "Account Type": "Savings", "Balance": 45000},
    {"Account Number": 1002, "Name": "Priya Verma", "Age": 28, "Account Type": "Current", "Balance": 75000},
    {"Account Number": 1003, "Name": "Rahul Mehta", "Age": 40, "Account Type": "Savings", "Balance": 32000},
    {"Account Number": 1004, "Name": "Sneha Patil", "Age": 35, "Account Type": "Current", "Balance": 91000},
    {"Account Number": 1005, "Name": "Vikas Singh", "Age": 45, "Account Type": "Savings", "Balance": 60000},
    {"Account Number": 1006, "Name": "Neha Joshi", "Age": 26, "Account Type": "Current", "Balance": 120000},
    {"Account Number": 1007, "Name": "Rohan Gupta", "Age": 38, "Account Type": "Savings", "Balance": 53000},
    {"Account Number": 1008, "Name": "Kavita Rao", "Age": 31, "Account Type": "Current", "Balance": 81000},
    {"Account Number": 1009, "Name": "Manoj Kumar", "Age": 50, "Account Type": "Savings", "Balance": 47000},
    {"Account Number": 1010, "Name": "Pooja Desai", "Age": 29, "Account Type": "Current", "Balance": 69000},
]


# step 2 : Deposit Money
# Implement a function to allow a user to deposit money into their account.
# Use a for loop to find the correct account and update the balance.

def deposit():
    pin = int(input("enter your account number : "))
    amount = int(input("enter a amount : "))
    for i in accounts:
        if pin == i["Account Number"]:
            print("OLD Amount : ",i["Balance"])
            print("New Amount : ",amount+i["Balance"])
            break
# deposit()

# step 3 : Withdraw Money
# Implement a function to allow a user to withdraw money.
# Use an if condition to check if the balance is sufficient before withdrawal.

def withdraw():
    pin = int(input("enter your account number : "))
    amount = int(input("enter amount : "))
    for i in accounts:
        if pin == i["Account Number"]:
            if amount < i["Balance"]:
                a =i["Balance"] - amount 
                print("Previous Balance : ",i["Balance"])
                print("Balance amount : ",a)
                break
            else:
                print("insufficient balance ")
# withdraw()

# step 4 : Check Balance
# Implement a function that allows a user to check their account balance.
# The function should search for the account using a for loop.

def Check_Balance():
    pin = int(input("enter your account number : "))
    for i in accounts:
        if pin == i["Account Number"]:
            print(i["Balance"])
            break
# Check_Balance()

# step 5 : Display All Account Holders
# Implement a function to display all customer details in a structured format.

def Details():
    df = pd.DataFrame(accounts,index=None)
    print(df.to_markdown(index=False))

# Details()

# step 6 : Filter High-Value Customers
# Use an if condition to display customers with a balance greater than a specified amount.

def greater_amount():
    new = []
    for i in accounts:
        new.append(i["Balance"])
    df=pd.DataFrame(new,columns=["Balance"])
    print(df.to_markdown(index=False))
    print("Highest Amount :",max(new))

   
# Find the account with the highest balance
    max_balance = max(accounts, key=lambda x: x['Balance'])

# Print the account number with the highest balance
    print("\nAccount with highest balance:")
    print(f"Account Number: {max_balance['Account Number']}, Balance: {max_balance['Balance']}")


greater_amount()
