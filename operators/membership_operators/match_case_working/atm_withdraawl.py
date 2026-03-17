# ATM Withdrawal

#Task:

#Ask for PIN.

#If PIN is correct:

#Ask for withdrawal amount

#If amount ≤ balance → "Withdrawal successful"

#Else → "Insufficient balance"

#Else → "Incorrect PIN"

dp_pin = "45678"
db_balance = 35000
user_pin = int(input("Enter PIN: "))
if dp_pin == user_pin:

    withdrawal_amount = input("withdrawal amount: ")

    if withdrawal_amount <= db_balance:
        
        print("Withdrawal successful")

    else:

        print("Insufficient balance")
        
else:
    
        print("Incorrect PIN")