import praw
import time

# Stores credentials
client_id = 'CLIENT_ID'
client_secret = 'CLIENT_SECRET'
username = 'USERNAME'
password = 'PASSWORD' 
user_agent = 'SCRIPT_NAME'

# Authenticate with Reddit API
reddit = praw.Reddit(
    client_id=client_id,
    client_secret=client_secret,
    username=username,
    password=password,
    user_agent=user_agent
)

# Delete all posts
print("Deleting posts...")
for submission in reddit.redditor(username).submissions.new(limit=None):
    print(f"Deleting post: {submission.title} ({submission.id})")
    submission.delete() 
    time.sleep(2) # Sleep to avoid rate limit

# Delete all comments
print("Deleting comments...")
for comment in reddit.redditor(username).comments.new(limit=None):
    print(f"Deleting comment: {comment.body[:30]}... ({comment.id})")  # Display first 30 characters of the comment
    comment.delete()  
    time.sleep(2) # Sleep to avoid rate limit

print("All posts and comments have been deleted!")
