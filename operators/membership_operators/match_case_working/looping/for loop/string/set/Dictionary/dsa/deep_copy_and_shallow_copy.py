# deep copy :-
# copy.py => deep copy

from copy import deepcopy

arun_favt_foods = [
    {"meal_type":"breakfast","meal":"dosa"},
    {"meal_type":"lunch","meal":"fish meal"},
    {"meal_type":"dinner","meal":"fried rice"},
]

hari_favt_foods = deepcopy(arun_favt_foods)

hari_favt_foods[0]["meal"] = "idly"

print("arun",arun_favt_foods)
print("hari",hari_favt_foods)


# shallow copy :-

arun_favt_colors = ["red","green","blue"]
hari_favt_colors = arun_favt_colors.copy()

hari_favt_colors[0] = "purple"
print("arun",arun_favt_colors)
print("hari",hari_favt_colors)

