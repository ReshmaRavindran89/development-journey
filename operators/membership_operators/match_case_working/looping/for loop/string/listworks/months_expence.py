
# JANUARY- DECEMBER

expense = [13000,14000,15000,16000,17000,18000,19000,14000,13500,15500,18500,19500]
        #    0     1     2     3     4      5      6     7    8     9     10   11

print(expense)

print(expense[2])

total_expense = 0

for exp in expense:
    total_expense+=exp

print("Total Expense",total_expense)
print("Avg expense",total_expense/len(expense))
