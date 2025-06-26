#A Python-based program simulating an ATM with PIN authentication, balance inquiry, deposit, and withdrawal functionality, using JSON for data storage
import json

with open("ATM simulation.json","r") as file:
    data = json.load(file)

pin = data['pin'] 
total_balance = data['total_balance']

menu_list = '''
        MENU
1. Check balance
2. Deposit money
3. Withdraw money
4. Exit
'''

choice = 0

def menu(total_balance):
    '''
        Argument (as Float): Total balance (from ATM simulation.json)

        Input (as Integer): Choice of operation

        It displays menu to user and calls function corresponding to the choice 

        Returns: Choice, Total balance
    '''
    print(menu_list)
    choice = int(input("Enter choice: "))
    if choice == 1:
        check_balance(total_balance)
        
    elif choice == 2:
        total_balance = deposit_money(total_balance)
        
    elif choice == 3:
        total_balance = withdraw_money(total_balance)
        
    elif choice == 4: 
        print("Thank you!")
        
    else:
        print("Enter valid choice (1-4)")
        
    return choice, total_balance
    # can declare total_balance as global 
    # we would only need to return choice

def check_balance(balance):
    '''
        Argument (as Float): Balance

        Input : None

        It displays Current Balance

        Returns: Nothing
    '''
    print(f"\nYour current balance is {balance} Rs.")

def deposit_money(balance):
    '''
        Argument (as Float): Balance

        Input (as Float): Amount to deposit in account

        It displays Amount deposited in the account

        Returns: Updated Balance
    '''
    deposit = float(input("Enter amount to deposit (in Rs): "))
    balance = balance + deposit
    print(f"\n{deposit} Rs Deposit successfully!")
    return balance

def withdraw_money(balance):
    '''
        Argument (as Float): Balance

        Input (as Float): Amount to withdraw from account

        It displays Amount withdrawed from the account

        Returns: Updated Balance
    '''
    withdraw = float(input("Enter amount to withdraw (in Rs): "))
    if withdraw > balance:
        print("\nInsufficient funds for withdrawal")
    else:
        balance = balance - withdraw
        print(f"\n{withdraw} Rs Withdrawed successfully!")
        return balance

welcome_mssg = "\t\t*** Welcome to ATM Machine Simulation ***"
print(welcome_mssg)

attempt = 0

while attempt<3 and choice != 4:
    pin_in = int(input("\nEnter your 4-digit pin: "))
    if pin_in == pin:
        print("Access granted!")
        while choice != 4:
            choice, total_balance = menu(total_balance) #if total_variable declared global then -> choice = menu() -> no arguments in the definition too
    else:
        print("Invalid pin!")
        attempt = attempt + 1

if attempt == 3:
    print("\nAccess not granted!")

data['total_balance'] = total_balance
with open("ATM simulation.json","w") as file_write:
    json.dump(data,file_write,indent=2)