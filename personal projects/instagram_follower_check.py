import instaloader

username = input("Username:")
password = input("Password:")
# make instance
loader = instaloader.Instaloader()

# Login using the credentials
loader.login(username, password)

# Use Profile class to access metadata of account
profile = instaloader.Profile.from_username(loader.context,
                                            username)

# get followers
followers = profile.get_followers()
followers_list = []
for follower in followers:
    followers_list.append(follower)

# get followees
followees = profile.get_followees()
followees_list = []
for followee in followees:
    followees_list.append(followee)


# compare lists and print who's not following back
not_following = set(followees_list) - set(followers_list)
for user in not_following:
    print(f"{user}\n")
    
