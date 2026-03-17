
fr =open("file operators\\orders.txt","r")

all_orders =[line.rstrip("\n")for line in fr]


#for line in fr:
    #cleaned_line = line.rstrip("\n")
   # all_orders.append(cleaned_line)

order_count = {o:all_orders.count(o) for o in all_orders}

print(order_count)


