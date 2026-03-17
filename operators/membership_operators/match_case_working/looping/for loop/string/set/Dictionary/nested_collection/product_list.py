
products = [
    [1, "iPhone 15", "Apple", "Electronics", 79999, 120],
    [2, "Galaxy S24", "Samsung", "Electronics", 74999, 150],
    [3, "MacBook Air M2", "Apple", "Electronics", 114999, 80],
    [4, "Air Jordan Shoes", "Nike", "Footwear", 12999, 200],
    [5, "Noise Smartwatch", "Noise", "Accessories", 2999, 300],
    [6, "HP Pavilion Laptop", "HP", "Electronics", 65000, 60],
    [7, "Levi's Jeans", "Levi's", "Clothing", 2499, 250],
    [8, "Boat Rockerz 450", "Boat", "Accessories", 1499, 500]
]

# 1. display all product names
# 2. product with the highest price
# 3. display electronics products
# 4. display products where the brand is Apple
# 5. which category has most products
# 6. product with maximum stock
# 7. list all categories


# which category has most products:-

all_categories = [p[3] for p in products]
category_count = {c:all_categories.count(c) for c in all_categories}
category_count_list = [[v,k] for k,v in category_count.items()]
print(sorted(category_count_list,reverse=True))
