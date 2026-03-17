

# W.A.P TO DISPLAY ALPHABET_COUNT,DIGIT_COUNT,SPECIAL_CHARACTER_COUNT.

word = "aman##aplan**panamawith2car1bike"

al_count = 0
d_count = 0
sp_count = 0

for ch in word:

    if ch.isalpha():
        al_count+=1

    elif ch.isdigit():
        d_count+=1

    elif not ch.isalnum():
        sp_count+=1

print(f"ALPHABET COUNT : {al_count}")
print(f"DIGIT COUNT : {d_count}")
print(f"SPECIAL CHARACTER COUNT : {sp_count}")

