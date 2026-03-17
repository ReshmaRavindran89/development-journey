"""
spam words :-

"""

def count_spam_words(words):

    count = 0

    fr=open("file operators\\error_handling\\spam_words.txt")

    spam_words=[line.rstrip("\n")for line in fr]

    clean_words=[w for w in words.split(" ") if w in spam_words]

    count=len(clean_words)

    print(len(clean_words)/len(words.split(" "))*100) # to find percentage

    return count

print(count_spam_words("you win free cash"))



