
# word count:-

text = "python programming programming is simple"

words_count = text.split(" ")
words_count = { w:words_count.count(w) for w in words_count } # ["python" "programming" "programming" "is" "simple"]

print(words_count)

# orders count:-

orders = ["tea","coffee","idly","coffee","tea","dosa","tea","coffee"]

order_count = {o:orders.count(o) for o in orders}
print(order_count)
