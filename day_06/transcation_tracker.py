"""
Docstring for day_06.transcation_tracker
"""

"""
Write a function named after_transaction() that returns the amount of money in an account after a transaction. 
The two parameters for this function are balance and transaction. 
They will both have integer arguments. 
The balance is how much money is currently in the account,
and the transaction is how much to add or remove from the account (based on whether transaction is a positive or negative integer).

This operation is more complicated than just return balance + transaction. If the transaction is negative and would overdraw the account (that is, if balance + transaction is less than zero), then the transaction should be ignored and the original balance returned. 
For example, calling the function from the interactive shell should look like this:

>>> after_transaction(500, 20)
520
>>> after_transaction(300, -200)
100
"""

def get_balance():
    global balance;

    try:
     balance=int(input("Enter the current balance: "))
     return balance
    except ValueError:
       print("Invalid input for balance. Please enter a valid integer.")
       return get_balance();
       



def get_transaction():
    global transaction;

    try:
     
     transaction=int(input("Enter the transaction amount (positive or negative): "))
     return transaction
    except ValueError:
       print("Invalid input for transaction. Please enter a valid integer.")
       return get_transaction();



def after_transaction(balance, transaction):
   if transaction==0:
      print(" Transaction ended by user print receipt .")
      return balance;
   elif balance + transaction < 0 and transaction < 0:
       print("Transaction would overdraw the account. Transaction ignored.")
       return balance;
   else:
         return balance + transaction;
 

def Transaction_Tracker():
   global balance;
   transaction=get_transaction();
   balance = after_transaction(balance, transaction);
   print("New balance is: ",balance);

   
    
balance=get_balance();

print("Current balance is: ",balance);
choice=True;
while choice:
   Transaction_Tracker();
   user_choice=input("Do you want to perform another transaction? (yes/no): ").strip().lower();
   if user_choice != 'yes' and user_choice != 'y':
       choice=False;



print("Thank you for using the transaction tracker. Goodbye!");

