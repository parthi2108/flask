import instaloader

# Initialize instaloader
L = instaloader.Instaloader()

# Login using your Instagram credentials
username = input("Enter your Instagram username: ")
password = input("Enter your Instagram password: ")

try:
    L.login(username, password)  # Log in to Instagram
    print("Login successful!")
except Exception as e:
    print(f"Login failed: {e}")
    exit()

# Fetch the profile for the logged-in user
profile = instaloader.Profile.from_username(L.context, username)

# Fetch the people you're following and your followers
following = set(followee.username for followee in profile.get_followees())
followers = set(follower.username for follower in profile.get_followers())

# 1. Count the total number of people you are following
total_following = len(following)

# 2. Find people you are following but are not following you back
not_following_back = following - followers

# Prepare the content to write into the file
content = f"Total people you are following: {total_following}\n"
content += "People not following you back:\n"
for user in not_following_back:
    content += f"- {user}\n"

# 3. Write the results to a text file
with open('following_report.txt', 'w') as file:
    file.write(content)

print("Report saved to 'following_report.txt'")
