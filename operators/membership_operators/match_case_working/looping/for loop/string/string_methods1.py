
# def isalpha() => return true if string is alphabet(one character or more character)
# def isdigit() => return true if string all are digits.
# def isalnum() => return true if string is alphanumeric.
# def startswith(self,prefix) =>
# def endswith(self,suffix) =>

word = "hello"
print(word.isalpha())

age = "23"
print(age.isdigit())

text = "hello23"
print(text.isalnum())

word1 = "luminar technolab"
print(word1.startswith("lu"))

word1 = "luminar technolab"
print(word1.endswith("lab"))

word1 = "luminar technolab"
print(f"left{word1.strip()}right")

word2 = "\nluminar technolab\t"
new_word = word2.lstrip("\n")
new_word = new_word.rstrip("\t")
print(new_word)
