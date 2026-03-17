
penguin_data = [
    {"region": "Anvers", "flipper_length": 181, "body_mass": 3750, "bill_length": 39.1, "bill_depth": 18.7},
    {"region": "Anvers", "flipper_length": 186, "body_mass": 3800, "bill_length": 39.5, "bill_depth": 17.4},
    {"region": "Biscoe", "flipper_length": 195, "body_mass": 3250, "bill_length": 40.3, "bill_depth": 18.0},
    {"region": "Dream", "flipper_length": 193, "body_mass": 3450, "bill_length": 36.7, "bill_depth": 19.3},
    {"region": "Biscoe", "flipper_length": 190, "body_mass": 3650, "bill_length": 39.3, "bill_depth": 20.6},
    {"region": "Dream", "flipper_length": 181, "body_mass": 3625, "bill_length": 38.9, "bill_depth": 17.8},
    {"region": "Anvers", "flipper_length": 191, "body_mass": 4675, "bill_length": 39.2, "bill_depth": 19.6},
    {"region": "Dream", "flipper_length": 198, "body_mass": 4675, "bill_length": 41.1, "bill_depth": 17.6},
    {"region": "Biscoe", "flipper_length": 185, "body_mass": 4250, "bill_length": 42.0, "bill_depth": 20.2},
    {"region": "Anvers", "flipper_length": 190, "body_mass": 3300, "bill_length": 37.8, "bill_depth": 17.1},
    {"region": "Biscoe", "flipper_length": 210, "body_mass": 4200, "bill_length": 46.1, "bill_depth": 13.2},
    {"region": "Biscoe", "flipper_length": 211, "body_mass": 4400, "bill_length": 50.0, "bill_depth": 16.3},
    {"region": "Dream", "flipper_length": 201, "body_mass": 4150, "bill_length": 48.7, "bill_depth": 14.1},
    {"region": "Anvers", "flipper_length": 210, "body_mass": 4500, "bill_length": 50.0, "bill_depth": 15.2},
    {"region": "Biscoe", "flipper_length": 215, "body_mass": 5700, "bill_length": 47.6, "bill_depth": 14.5},
    {"region": "Dream", "flipper_length": 210, "body_mass": 5350, "bill_length": 46.5, "bill_depth": 13.5},
    {"region": "Anvers", "flipper_length": 213, "body_mass": 4400, "bill_length": 45.4, "bill_depth": 14.6},
    {"region": "Biscoe", "flipper_length": 219, "body_mass": 4850, "bill_length": 46.7, "bill_depth": 15.3},
    {"region": "Dream", "flipper_length": 209, "body_mass": 5000, "bill_length": 43.3, "bill_depth": 13.4},
    {"region": "Anvers", "flipper_length": 220, "body_mass": 5950, "bill_length": 46.8, "bill_depth": 16.1},
    {"region": "Biscoe", "flipper_length": 222, "body_mass": 5200, "bill_length": 40.9, "bill_depth": 13.7},
    {"region": "Dream", "flipper_length": 208, "body_mass": 4900, "bill_length": 49.0, "bill_depth": 16.1},
    {"region": "Anvers", "flipper_length": 215, "body_mass": 4075, "bill_length": 50.6, "bill_depth": 19.4},
    {"region": "Biscoe", "flipper_length": 210, "body_mass": 3725, "bill_length": 46.0, "bill_depth": 18.5},
    {"region": "Dream", "flipper_length": 210, "body_mass": 3650, "bill_length": 51.3, "bill_depth": 19.2},
    {"region": "Anvers", "flipper_length": 193, "body_mass": 3350, "bill_length": 45.4, "bill_depth": 18.7},
    {"region": "Biscoe", "flipper_length": 210, "body_mass": 4050, "bill_length": 52.7, "bill_depth": 19.8},
    {"region": "Dream", "flipper_length": 197, "body_mass": 3675, "bill_length": 45.2, "bill_depth": 17.8},
    {"region": "Anvers", "flipper_length": 202, "body_mass": 4100, "bill_length": 46.1, "bill_depth": 18.2},
    {"region": "Biscoe", "flipper_length": 205, "body_mass": 3775, "bill_length": 51.3, "bill_depth": 18.2},
    {"region": "Dream", "flipper_length": 195, "body_mass": 4000, "bill_length": 46.0, "bill_depth": 18.9},
    {"region": "Anvers", "flipper_length": 210, "body_mass": 4100, "bill_length": 51.3, "bill_depth": 19.9},
    {"region": "Biscoe", "flipper_length": 187, "body_mass": 3550, "bill_length": 46.6, "bill_depth": 17.8},
    {"region": "Dream", "flipper_length": 201, "body_mass": 4300, "bill_length": 51.7, "bill_depth": 20.3},
    {"region": "Anvers", "flipper_length": 196, "body_mass": 3400, "bill_length": 47.0, "bill_depth": 17.3},
    {"region": "Biscoe", "flipper_length": 210, "body_mass": 4450, "bill_length": 52.0, "bill_depth": 18.1},
    {"region": "Dream", "flipper_length": 203, "body_mass": 4500, "bill_length": 45.9, "bill_depth": 17.1},
    {"region": "Anvers", "flipper_length": 190, "body_mass": 3575, "bill_length": 50.5, "bill_depth": 18.4},
    {"region": "Biscoe", "flipper_length": 212, "body_mass": 4300, "bill_length": 50.3, "bill_depth": 20.0},
    {"region": "Dream", "flipper_length": 202, "body_mass": 3700, "bill_length": 58.0, "bill_depth": 17.8},
    {"region": "Anvers", "flipper_length": 180, "body_mass": 3000, "bill_length": 46.4, "bill_depth": 18.6},
    {"region": "Biscoe", "flipper_length": 191, "body_mass": 3800, "bill_length": 49.2, "bill_depth": 18.2},
    {"region": "Dream", "flipper_length": 196, "body_mass": 3950, "bill_length": 42.4, "bill_depth": 17.3},
    {"region": "Anvers", "flipper_length": 193, "body_mass": 3400, "bill_length": 48.5, "bill_depth": 15.0},
    {"region": "Biscoe", "flipper_length": 190, "body_mass": 4475, "bill_length": 43.2, "bill_depth": 18.5},
    {"region": "Dream", "flipper_length": 199, "body_mass": 4100, "bill_length": 50.6, "bill_depth": 19.4},
    {"region": "Anvers", "flipper_length": 191, "body_mass": 3550, "bill_length": 46.7, "bill_depth": 17.9},
    {"region": "Biscoe", "flipper_length": 195, "body_mass": 4200, "bill_length": 52.0, "bill_depth": 19.0},
    {"region": "Dream", "flipper_length": 193, "body_mass": 3800, "bill_length": 50.5, "bill_depth": 15.9},
    {"region": "Anvers", "flipper_length": 205, "body_mass": 4150, "bill_length": 49.5, "bill_depth": 19.0},
    {"region": "Biscoe", "flipper_length": 190, "body_mass": 3950, "bill_length": 46.2, "bill_depth": 14.5},
    {"region": "Dream", "flipper_length": 203, "body_mass": 3725, "bill_length": 50.1, "bill_depth": 17.9},
    {"region": "Anvers", "flipper_length": 195, "body_mass": 3650, "bill_length": 46.5, "bill_depth": 17.9},
    {"region": "Biscoe", "flipper_length": 201, "body_mass": 4050, "bill_length": 45.0, "bill_depth": 15.4},
    {"region": "Dream", "flipper_length": 196, "body_mass": 3525, "bill_length": 50.8, "bill_depth": 19.0},
    {"region": "Anvers", "flipper_length": 193, "body_mass": 3725, "bill_length": 46.1, "bill_depth": 18.2},
    {"region": "Biscoe", "flipper_length": 195, "body_mass": 3325, "bill_length": 52.1, "bill_depth": 17.0},
    {"region": "Dream", "flipper_length": 191, "body_mass": 3950, "bill_length": 46.8, "bill_depth": 15.4},
    {"region": "Anvers", "flipper_length": 194, "body_mass": 3800, "bill_length": 45.7, "bill_depth": 17.0},
    {"region": "Biscoe", "flipper_length": 200, "body_mass": 3900, "bill_length": 55.8, "bill_depth": 19.8},
    {"region": "Dream", "flipper_length": 187, "body_mass": 3150, "bill_length": 43.5, "bill_depth": 18.1},
    {"region": "Anvers", "flipper_length": 201, "body_mass": 3400, "bill_length": 49.6, "bill_depth": 18.2},
    {"region": "Biscoe", "flipper_length": 190, "body_mass": 4275, "bill_length": 50.8, "bill_depth": 19.0},
    {"region": "Dream", "flipper_length": 192, "body_mass": 3800, "bill_length": 46.2, "bill_depth": 17.5},
    {"region": "Anvers", "flipper_length": 203, "body_mass": 4150, "bill_length": 50.7, "bill_depth": 19.7},
    {"region": "Biscoe", "flipper_length": 192, "body_mass": 3500, "bill_length": 46.1, "bill_depth": 17.4},
    {"region": "Dream", "flipper_length": 200, "body_mass": 4300, "bill_length": 51.3, "bill_depth": 19.2},
    {"region": "Anvers", "flipper_length": 208, "body_mass": 4450, "bill_length": 46.6, "bill_depth": 17.8},
    {"region": "Biscoe", "flipper_length": 197, "body_mass": 3750, "bill_length": 51.9, "bill_depth": 16.7},
    {"region": "Dream", "flipper_length": 212, "body_mass": 4775, "bill_length": 52.2, "bill_depth": 18.8},
    {"region": "Anvers", "flipper_length": 187, "body_mass": 3600, "bill_length": 49.5, "bill_depth": 17.5},
    {"region": "Biscoe", "flipper_length": 210, "body_mass": 4000, "bill_length": 50.8, "bill_depth": 17.3},
    {"region": "Dream", "flipper_length": 200, "body_mass": 4500, "bill_length": 50.1, "bill_depth": 18.9},
    {"region": "Anvers", "flipper_length": 205, "body_mass": 4250, "bill_length": 49.0, "bill_depth": 19.6},
    {"region": "Biscoe", "flipper_length": 210, "body_mass": 3950, "bill_length": 51.5, "bill_depth": 18.7},
    {"region": "Dream", "flipper_length": 193, "body_mass": 3400, "bill_length": 49.8, "bill_depth": 17.3},
    {"region": "Anvers", "flipper_length": 198, "body_mass": 3725, "bill_length": 48.1, "bill_depth": 16.4},
    {"region": "Biscoe", "flipper_length": 203, "body_mass": 4350, "bill_length": 51.4, "bill_depth": 19.0},
    {"region": "Dream", "flipper_length": 187, "body_mass": 3525, "bill_length": 40.7, "bill_depth": 17.0},
    {"region": "Anvers", "flipper_length": 185, "body_mass": 3700, "bill_length": 46.5, "bill_depth": 17.9},
    {"region": "Biscoe", "flipper_length": 210, "body_mass": 4400, "bill_length": 50.3, "bill_depth": 20.0},
    {"region": "Dream", "flipper_length": 210, "body_mass": 3550, "bill_length": 49.3, "bill_depth": 19.9},
    {"region": "Anvers", "flipper_length": 197, "body_mass": 3800, "bill_length": 50.1, "bill_depth": 17.9},
    {"region": "Biscoe", "flipper_length": 218, "body_mass": 4775, "bill_length": 46.5, "bill_depth": 14.8},
    {"region": "Dream", "flipper_length": 215, "body_mass": 5650, "bill_length": 50.0, "bill_depth": 15.3},
    {"region": "Anvers", "flipper_length": 214, "body_mass": 5200, "bill_length": 51.3, "bill_depth": 14.2},
    {"region": "Biscoe", "flipper_length": 215, "body_mass": 5500, "bill_length": 47.5, "bill_depth": 15.0},
    {"region": "Dream", "flipper_length": 212, "body_mass": 5300, "bill_length": 52.2, "bill_depth": 17.1},
    {"region": "Anvers", "flipper_length": 217, "body_mass": 5550, "bill_length": 45.2, "bill_depth": 15.8},
    {"region": "Biscoe", "flipper_length": 228, "body_mass": 6300, "bill_length": 49.4, "bill_depth": 15.8},
    {"region": "Dream", "flipper_length": 225, "body_mass": 5400, "bill_length": 41.7, "bill_depth": 14.7},
    {"region": "Anvers", "flipper_length": 216, "body_mass": 4750, "bill_length": 46.2, "bill_depth": 14.1},
    {"region": "Biscoe", "flipper_length": 221, "body_mass": 5350, "bill_length": 51.5, "bill_depth": 16.3},
    {"region": "Dream", "flipper_length": 221, "body_mass": 5550, "bill_length": 46.2, "bill_depth": 14.4},
    {"region": "Anvers", "flipper_length": 222, "body_mass": 5750, "bill_length": 47.3, "bill_depth": 15.3},
    {"region": "Biscoe", "flipper_length": 224, "body_mass": 5850, "bill_length": 44.5, "bill_depth": 14.3},
    {"region": "Dream", "flipper_length": 229, "body_mass": 5950, "bill_length": 48.8, "bill_depth": 16.2},
    {"region": "Anvers", "flipper_length": 225, "body_mass": 5250, "bill_length": 47.2, "bill_depth": 13.7},
    {"region": "Biscoe", "flipper_length": 230, "body_mass": 6050, "bill_length": 49.1, "bill_depth": 14.8},
    {"region": "Dream", "flipper_length": 217, "body_mass": 5200, "bill_length": 44.9, "bill_depth": 13.3}
]

# display all regions:-

all_regions = [p.get("region") for p in penguin_data]
all_regions_list = len(penguin_data)
print(all_regions)

# display no of regions:-

all_regions = len(penguin_data)
print(all_regions)

# display unique region:-

unique_region = {p.get("region") for p in penguin_data}
print(unique_region)

# display flipper length:-
flipper_length = [p.get("flipper_length") for p in penguin_data]
print(flipper_length)

# display highest flipper length:-

highest_flipper = max(penguin_data,key=lambda p:p.get("flipper_length"))
print(highest_flipper)

# display lowest flipper length:-


lowest_flipper = min(penguin_data,key=lambda p:p.get("flipper_length"))
print(lowest_flipper)

# display total of flipper length:-

total_flipper = sum(flipper_length)
print(total_flipper)

# display avg flipper length:-

avg_flipper = total_flipper / all_regions_list
print(avg_flipper)

# display body mass:-

body_mass = [p.get("body_mass") for p in penguin_data]
body_mass_list = len(penguin_data)
print(body_mass_list)

# display highest body mass:-

highest_body_mass = max(penguin_data,key=lambda p:p.get("body_mass"))
print(highest_body_mass)

# display lowest body mass:-

lowest_flipperest_body_mass = min(penguin_data,key=lambda p:p.get("body_mass"))
print(lowest_flipperest_body_mass)

# display bill length:-

bill_length = [p.get("bill_length") for p in penguin_data]
bill_length_list = len(penguin_data)
print(bill_length)

# display no of bill length:-

bill_length_list = len(penguin_data)
print(bill_length_list)

# display highest bill length:-

highest_bill_length = max(penguin_data,key=lambda p:p.get("bill_length"))
print(highest_bill_length)

# display lowest bill length:-

lowest_bill_length = min(penguin_data,key=lambda p:p.get("bill_length"))
print(lowest_bill_length)

# display total bill length:-

total_bill_length = sum(bill_length)
print(total_bill_length)


# avg bill length:-

avg_bill_length = total_bill_length / all_regions_list
print(avg_bill_length)

# display bill_depth:-

bill_depth = [p.get("bill_depth") for p in penguin_data]
bill_depth_list = len(penguin_data)
print(bill_depth)

# display highest bill_depth:-

highest_bill_depth = max(penguin_data,key=lambda p:p.get("bill_depth"))
print(highest_bill_depth)

# display lowest bill depth:-

lowest_bill_depth = min(penguin_data,key=lambda p:p.get("bill_depth"))
print(lowest_bill_depth)

# total bill depth:-

total_bill_depth = sum(bill_depth)
print(total_bill_depth)

# avg bill depth:-

avg_bill_depth = total_bill_depth / all_regions_list
print(avg_bill_depth)

