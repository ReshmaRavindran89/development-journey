# stop words removing :-


def remove_stop_words(sentence):

    result=""

    fr = open("file operators\\error_handling\\stop_words.txt")

    stop_words = [line.rstrip("\n") for line in fr]    

    cleaned_words = [w for w in sentence.split(" ") if w not in stop_words]

    result = " ".join(cleaned_words)

    return result

sentence2="machine learning is a subset of AI"
sentence3="django is a one of python framework"

print(remove_stop_words(sentence2))


assert remove_stop_words(sentence2)=="machine learning subset AI","test case1 failed"
assert remove_stop_words(sentence3)=="django one python framework","test case2 failed"

print("code accepted....")

