
# comprehension :-

# list -> list comprehension.

#[left middle right]

# [return iteration condition]

arr = [10,12,13,14,15]
squares = [num**2 for num in arr]
print(squares)

cubes = [num**3 for num in arr]
print(cubes)

add_ten = [num+10 for num in arr]
print(add_ten)

sub_five = [num-5 for num in arr]
print(sub_five)

# display number list from 1 to 10:-

number_list = [i for i in range(1,11)]
print(number_list)

# create a list that contains double of each other :- 
nums = [2,4,6,8,10]

double_by_two = [num*2 for num in nums]
print(double_by_two)

# create a list of even number from range of 20 to 50 :-

even_number_list = [i for i in range(20,51,2)]
print(even_number_list)

# Another  method:-

even_number_list = [i for i in range(20,51) if i%2==0]
print(even_number_list)

# create a new list that contain words length > 3 :-

words=["apple","bat","carrot","elephant","ball","red"]

word_length  = [ w for w in words if len(w)>3]
print(word_length)

# create a new collection that contain recursive numbers:-

nums = [10,11,10,11,12,13,14,15,16,15] 

recursive = {n for n in nums if nums.count(n)>1} # here we need only repeated numbers to display thats why we use set.
print(recursive)

# create a new list that contain palindrome words :-

words = ["mad","test","tan","dad","stats","racecar"]

palindrome_words = [w for w in words if w [::-1]==w]
print(palindrome_words)

# display key and value :-

lst = [10,11,12,11,10,13,13]

# o/p {10: 2, 11: 2, 12: 1, 13: 2}

num_count ={n:lst.count(n) for n in lst}
print(num_count)

# display character count :-

word = "racecar"

character_count = {ch:word.count(ch) for ch in word}
print(character_count)

# print non recursive character.
# print recursive character whose count > 2 .
# anagram words = {listen}

lst1 = ["listen","earth","moon","dad","madam","race"]
lst2 = ["slient","angel","heart","test","dam","care"]

word  = "racecarfast"
non_recursive_character = { ch for ch in word if word.count(ch)==1}

recursive_character = { ch:word.count(ch) for ch in word if word.count(ch)>2}

print(non_recursive_character)
print(recursive_character)