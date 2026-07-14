# atm.py file
import pandas as pd

df = pd.read_csv(r"C:\Users\makys\OneDrive\Desktop\Python\Banking_Details\bank_accounts.csv")


def Check_Balance(account_No):
    account = df[df["Account No"] == account_No]
    balance = account.iloc[0]["Current Balance"]
    print("Current Balance:", balance)

def deposit(account_No):
    global df

    Cr_Amount = float(input("Enter Amount to be Deposited: "))

    # find index of account
    idx = df[df["Account No"] == account_No].index[0]

    # update deposit
    df.at[idx, "Deposit"] += Cr_Amount

    # update balance
    df.at[idx, "Current Balance"] += Cr_Amount

    # save back to CSV
    df.to_csv(r"C:\Users\makys\OneDrive\Desktop\Python\Banking_Details\bank_accounts.csv", index=False)

    print("Deposit successful!")
    
    Check_Balance(account_No)


def withdrawal(account_No):

    global df

    dr_Amount = float(input("Enter Amount to be Withdraw: "))
    
    idx = df[df["Account No"] == account_No].index[0]
    df.at[idx, "Withdrawal"] += dr_Amount
    df.at[idx, "Current Balance"] -= dr_Amount
    df.to_csv(r"C:\Users\makys\OneDrive\Desktop\Python\Banking_Details\bank_accounts.csv", index=False)

    print("Withdrawal successful!")
    Check_Balance(account_No)
    

def Check_Account_Type(account_No):
    account = df[df["Account No"] == account_No]
    Account_type = account.iloc[0]["Account Type"]
    print("Account Type :",Account_type)

while True:

    account_input = input("\nEnter your Account No (or type EXIT): ")

    if account_input.lower() == "exit":
        print("Program Ended. Goodbye!")
        break

    if not account_input.isdigit():
        print("Invalid input. Try again.")
        continue

    account_No = int(account_input)

    if account_No not in df["Account No"].values:
        print("Invalid Account Number.")
        continue

    while True:

        print("""
        1. Check Balance
        2. Deposit
        3. Withdrawal
        4. Check Account Type
        5. Exit Account
        """)

        choice = input("Enter your choice: ")

        if choice == "5" or choice.lower() == "exit":
            print("Exiting account...\n")
            break

        match choice:

            case "1":
                Check_Balance(account_No)

            case "2":
                deposit(account_No)

            case "3":
                withdrawal(account_No)

            case "4":
                Check_Account_Type(account_No)

            case _:
                print("Invalid choice")
