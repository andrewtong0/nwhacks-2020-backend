import praw

USER_AGENT = "Get user comment history"
CLIENT_SECRET = "Orvb3JIRO9CX11Cpbl09Kspv38w"
CLIENT_ID = "LA50C53o0Zk27w"

reddit = praw.Reddit(client_id=CLIENT_ID,
                     client_secret=CLIENT_SECRET,
                     user_agent=USER_AGENT)
reddit.read_only = True

subreddit = reddit.subreddit("funny")


class RedditUser:
    def __init__(self, username):
        self.reddit_name = username
        self.reddit_content = get_user_content(username)


class Comment:
    def __init__(self, id, text, datetime):
        self.id = id
        self.text = text
        self.datetime = datetime


def get_user_content(username):
    output = []
    user = reddit.redditor(username)
    for comment in user.comments.new(limit=25):
        output.append(Comment(comment.id, comment.body, comment.created_utc))
    return output


# testUser = UserInformation("sodypop")
# for comment in testUser.reddit_content:
#     print(comment.text)
