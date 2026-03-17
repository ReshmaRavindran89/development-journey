







correct_pin = 1234
balance = 5000

entered_pin = int(input("Enter your PIN: "))

# Step 2: Check if PIN is correct
if entered_pin == correct_pin:
    # Step 3: PIN is correct, now ask for amount
    amount = int(input("Enter withdrawal amount: "))
    
    # Step 4: Check if enough balance exists
    if amount <= balance:
        print("Withdrawal successful")
    else:
        print("Insufficient balance")
        
else:
    # PIN was wrong from the start
    print("Incorrect PIN")