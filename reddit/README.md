# Reddit Comment Scraping

This is a small and simple script for reddit comment scraping!

---

## Installation:

To use this script you will need multiple dependencies:

### PRAW

Install the reddit API wrapper praw with:

```
pip install praw
```

Or, if you want to install praw for conda environment use:

```
conda install -c conda-forge praw
```

### pandas

pandas comes preinstalled with anaconda.
Alterantively, you can install pandas with:

```
pip install pandas
```

---

## Usage:

To use this specific script, clone the repository or download the reddit folder.

### Configuration

Then configure the ***config.txt*** file with your information.

This information can be obtained by [creating a new reddit app at this link.](https://reddit.com/prefs/apps)

Create a new app, give it a memorable name, and set your redirect uri to http://localhost:8080.

Your **client id** is the bolded alphanumeric string underneath the name of your app.
Your **secret** will be following the field *secret*.
Your **user agent** will be in the field *name*.

Please consult the official documentation for PRAW for more information: 
[https://praw.readthedocs.io/](https://praw.readthedocs.io/)

### Arguments

This script was designed to be ran from the command line.

It takes 1-2 positional arguments as such:

```
python reddit_scrape.py [SUBREDDIT] [LIMIT]
```

**[SUBREDDIT]** : The subreddit to scrape comments from

**[LIMIT]** : The number of comments to scrape. If omitted, the script will attempt to scrape all comments.

