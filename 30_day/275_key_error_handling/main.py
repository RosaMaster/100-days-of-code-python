facebook_posts = [
    {'Likes': 21, 'Comments': 2},
    {'Likes': 13, 'Comments': 2},
    {'Likes': 33, 'Comments': 8}
]

total_likes = 0
# Catch the KeyError exception in the dictionary
for post in facebook_posts:
    try:
        total_likes = total_likes + post['Likes']
    except KeyError:
        pass

print(total_likes)

