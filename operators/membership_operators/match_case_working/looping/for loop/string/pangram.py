
# pangram
alphabets = "abcdefghijklmnopqrstuvwxyz"

word = "The quick brown fox jumps over the lazy dog."

is_pangarm = True

for ch in alphabets:

    if ch not in word:
        is_pangarm = False
        break
    
print(is_pangarm)
