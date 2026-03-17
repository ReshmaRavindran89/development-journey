
"""
account_number
holder_name
balance
tasks:
deposit 5000
withdraw 2000
check balance is less than 1000 -> print "Low Balance"

"""

customer_account = {"account_number":32412,"holder_name":"rudra","balance":9000}

customer_account["balance"]+=5000

print(customer_account)

if customer_account["balance"]>2000:

    customer_account["balance"]-=2000

else:
    print("inSufficent Balance")

if customer_account["balance"]<1000:

    print("Low Balance")
