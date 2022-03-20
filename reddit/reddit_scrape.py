# Author: Jordan Myers
# A simple reddit comment scraping script!

### Imports ###
import praw
import pandas as pd
import sys
###############

### Functions ###

def save_comments_to_csv(sr:str, limit:int):
    if limit == 0:
        subhelper = reddit.subreddit(subreddit).comments()
    else:
        subhelper = reddit.subreddit(subreddit).comments(limit=limit)

    comments = []
    for comment in subhelper:
        comments.append([comment.parent_id, comment.body])
    
    comments = pd.DataFrame(comments, columns=["parent_id","comment"])
    comments.to_csv("comment_output.csv")

###############

# Read from config.txt for PRAW setup
config = {}
with open('config.txt') as f:
    for line in f.readlines():
        var,val = line.split(sep=":")
        config[var.strip()] = val.strip()


# Initialize reddit object
reddit = praw.Reddit(client_id = config['client_id'], client_secret = config['client_secret'], user_agent = config['user_agent'])

# parse args, set defaults, run script
argv = sys.argv

if(len(argv) < 2):
    print('No specificed arguments')
else:
    subreddit = argv[1]
    limit = 0
    if(len(argv) > 2):
        limit = int(argv[2])
    
    if(type(subreddit) != str or type(limit) != int):
        raise ValueError("Improper type for arguments")

    save_comments_to_csv(subreddit, limit)

