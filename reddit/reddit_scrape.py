# Author: Jordan Myers
# A simple reddit comment scraping script!

### Imports ###
import praw
from pmaw import PushshiftAPI
import pandas as pd

from typing import List
import datetime as dt
import argparse
###############

### Helper Functions ###

def save_comments_to_csv(reddit:praw.Reddit, pushshift:PushshiftAPI, limit:int, sr:List[str],usepush:bool,start_time:str):
    if limit == 0: l = None 
    else: l = limit
    
    if start_time is not None:
        y,m,d = start_time.split('-')
        start = int(dt.datetime(int(y),int(m),int(d)).timestamp())
    else: 
        start = None


    columns = ["subreddit","parent_id","created_utc","comment"]
    comment_df = pd.DataFrame(columns=columns)

    if usepush:
        for sub in sr:
            if start is not None:
                subhelper = pushshift.search_comments(after=start,subreddit=sub,limit=l,filter=['subreddit','parent_id','created_utc','body'])
            else:
                subhelper = pushshift.search_comments(subreddit=sub,limit=l,filter=['subreddit','parent_id','created_utc','body'])

            comments = []
            for comment in subhelper:
                comments.append([comment['subreddit'],comment['parent_id'], comment['created_utc'], comment['body']])
        
            comment_df = pd.concat([comment_df,pd.DataFrame(comments,columns=columns)])
    else:
        for sub in sr:
            subhelper = reddit.subreddit(sub).comments(limit=l)

            comments = []
            for comment in subhelper:
                comments.append([comment.subreddit,comment.parent_id,comment.created_utc, comment.body])
        
            comment_df = pd.concat([comment_df,pd.DataFrame(comments,columns=columns)])
        
    comment_df.to_csv("comment_output.csv")


###############

def run():
    
    # parse args, set defaults
    parser = argparse.ArgumentParser(description="Scrape subreddits for comments.")
    parser.add_argument('subreddit', type=str, nargs='+', action='append')
    parser.add_argument('limit', type=int, nargs=1)
    parser.add_argument('-p','--pushshift', dest='pushshift',action='store_true')
    parser.add_argument('-st','--starttime',dest='start',type=str,nargs=1,default=None)

    args = parser.parse_args()
    argv = vars(args)

    # Read from config.txt for PRAW setup
    config = {}
    with open('config.txt') as f:
        for line in f.readlines():
            var,val = line.split(sep=":")
            config[var.strip()] = val.strip()


    # Initialize reddit object
    reddit = praw.Reddit(client_id = config['client_id'], client_secret = config['client_secret'], user_agent = config['user_agent'])
    api = PushshiftAPI()

    save_comments_to_csv(reddit, api, argv['limit'][0], argv['subreddit'][0],argv['pushshift'],argv['start'][0])


# Only operate if main
if __name__ == '__main__':
    run()