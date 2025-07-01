items = {}
cust_name = input("Enter customer name: ").title()
date = input("Enter today's date (dd/mm/yyyy): ")

grocery_bill = f'''
                    GROCERIES
---------------------------------------------------
| Customer: {cust_name[:16].ljust(18)}| Date: {date[:11].ljust(12)}|
| {cust_name[16:42].ljust(28)}| {date[11:28].ljust(18)}|  
---------------------------------------------------
| Sr No. |         Item Name          |   Price   |
---------------------------------------------------'''

def get_groceries():
    '''
        Argument: None

        Input: Item name (as String)
               Item price (as Float)

        It takes item name as input 
            if item name is 'n' it terminates the loop
            else it stores item name(as key) & price(as value) in dictionary 'item{}'
        
        It verifys user input for price 
            if input is not float it handles it (ValueError)

        Returns: Nothing
    '''
    while True:
        item_name = input("\nEnter item name (or type n to stop): ").title()
        if item_name.lower() == 'n':
            break
        try:
            price = float(input(f"Enter price of '{item_name}': "))
            items[item_name] = price
        except ValueError:
            print("Please enter valid price!")

def bill():
    '''
        Argument: None

        Input: None

        It creates a grocery bill in text file named after customer

        Returns: Nothing
    '''
    total = 0
    with open(f"{cust_name}'s grocery.txt","w") as file:
        file.write(grocery_bill)
        for i,(i_name,price) in enumerate(items.items(),start=1):
            file.write(f"\n| {str(i).ljust(7)}| {i_name[:27].ljust(27)}| {str(price)[:10].ljust(10)}|")
            total = total + price
        file.write("\n"+("-"*51))
        file.write(f"\n| Total Price:                        | {str(total)[:10].ljust(10)}|")
        file.write("\n"+("-"*51))
        file.write("\n\n              THANK YOU! VISIT AGAIN")

#calling get_groceries() & bill()
get_groceries()
bill()

with open(f"{cust_name}'s grocery.txt","r") as file:
    final_bill = file.read()
print(final_bill)

print("\nBill is ready to print!") 
print(f"Saved as {cust_name}'s grocery.txt")
