"""
Setting up RedditAPI Connection for LUNA✱ Discord Bot
Created by Andrew
"""

import praw
REDDIT_CLIENT_ID = 'lVopHlk3hSgTpUk2dz7tpw'
REDDIT_CLIENT_SECRET = '5R6nJUpxWQ9rQWmTj3kqmz5MsKD7Hg'
REDDIT_USER_AGENT = 'lunareddit'
reddit = praw.Reddit(
    client_id=REDDIT_CLIENT_ID,
    client_secret=REDDIT_CLIENT_SECRET,
    user_agent=REDDIT_USER_AGENT,
    check_for_async=False
)
