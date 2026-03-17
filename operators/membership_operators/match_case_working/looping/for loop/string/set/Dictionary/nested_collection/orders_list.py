# order list:- 

orders={"tea":15,"coffee":21,"dosa":34,"rice":67}

order_list = [[v,k] for k,v in orders.items()]
print(sorted(order_list,reverse=True))


languages=["thamil","malayalam","kannada","telungu","kannada","telungu","thamil","malayalam","thamil","malayalam"]

language_count = {l:languages.count(l)for l in languages}
language_list = [[v,k] for k,v in language_count.items()]
print(sorted(language_list,reverse=True))
