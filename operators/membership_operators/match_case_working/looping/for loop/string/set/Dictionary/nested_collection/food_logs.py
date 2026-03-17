

social_media_posts = [

    [1,"good morning", 500,600,"amir"],
    [2,"goodafetrnoon",700,800,"arun"],
    [3,"goodevening ",700,800,"joy"],
    [4,"goodnight ", 900,950,"don"],
]

print(social_media_posts[1][2])

all_facebook_views = [lst[2] for lst in social_media_posts]
print(all_facebook_views)

all_insta_views = [lst[3]for lst in social_media_posts]
print(all_insta_views)

all_names = [lst[4] for lst in social_media_posts]
print(all_names)

all_posts = [lst[1] for lst in social_media_posts]
print(all_posts)

all_id = [lst[0] for lst in social_media_posts]
print(all_id)

all_insta_views =[lst[4]for lst in social_media_posts ]
print(all_insta_views)

max_insta_views = max([lst[2] for lst in social_media_posts])
max_insta_views = [lst[4] for lst in social_media_posts if lst[2]==max_insta_views]
print(max_insta_views)

min_insta_views = min([lst[2] for lst in social_media_posts])
min_insta_views = [lst[4] for lst in social_media_posts if lst[2]==min_insta_views]
print(min_insta_views)
 