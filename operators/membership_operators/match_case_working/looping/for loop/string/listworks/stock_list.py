
# update stock list.

stock_list1 = [10,11,12,13,14,15]
stock_list2 = [20,21,22,23,24,25]

# updated stock list will be by adding 5 => [15,16,17,18,19,20,25,26,27,28,29,30]

combined_list = stock_list1 + stock_list2
updated_stock_list = []

for num in combined_list:
    updated_stock_list.append(num + 5)

print(updated_stock_list)