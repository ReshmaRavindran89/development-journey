


# display all movie title.
# movie with top rating.
# display kannada movies.
# display movies whre actor is yash.
# which language most number of movies.  (hint: all_lang = ["k","m","k","t"])
# movie with max budget.
# languages.



movies = [
    [1, "K.G.F: Chapter 1", "Yash", "Kannada", 8.2, 1234567],
    [2, "K.G.F: Chapter 2", "Yash", "Kannada", 8.3, 678900],
    [3, "K.G.F: Chapter 3", "Yash", "Kannada", 9.5, 456789], # Anticipated
    [4, "Salaar: Part 1 – Ceasefire", "Prabhas", "Telugu", 6.5, 45678567],
    [5, "Pushpa 2: The Rule", "Allu Arjun", "Telugu", 10.0, 1234567], # Hype Rating
    [6, "Aavesham", "Fahadh Faasil", "Malayalam", 7.9, 1234567]
]


# display all movie title:-

all_movies_title = [lst[1]for lst in movies]
print(all_movies_title)

# movie with top rating:-

max_rating =max( [lst[4] for lst in movies])
top_movies = [lst[1] for lst in movies if lst[4]== max_rating]
print(top_movies)

# display kannada movies:-

kannada_movies = [lst[1] for lst in movies if lst[3] == "Kannada"]
print(kannada_movies)

# display movies where actor is yash:-

yash_movies = [lst[1] for lst in movies if lst[2] == "Yash"]
print(yash_movies)

# movie with max budget:-

max_budget = max([lst[5] for lst in movies])
movie_with_max_budget = [lst[1] for lst in movies if lst[5] == max_budget]
print(movie_with_max_budget)


# display language counts:-

languages_list = [m[3] for m in movies]
language_count = {l:languages_list.count(l)for l in languages_list}
language_count_list = [[v,k] for k,v in language_count.items()]
print(sorted(languages_list,reverse=True)[0])

