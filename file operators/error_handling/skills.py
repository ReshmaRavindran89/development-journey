def data_skill_set(skill):
     
     result=""

fr = open("file operators\\error_handling\\skills.txt")

stop_words = [line.rstrip("\n") for line in fr]    

cleaned_words = [w for w in sentence.split(" ") if w not in stop_words]

result = " ".join(cleaned_words)

return result