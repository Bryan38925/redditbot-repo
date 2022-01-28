# **Reddit Chuck Norris Joke Comment Bot**

This bot is made with python and will respond a random joke to comments in a subreddit.

* Choose subreddit where bot will be active
* Label keywords the bot will respond to

## Requirements

* Reddit Account
* [Python](https://www.python.org/downloads/)
* [Praw](https://praw.readthedocs.io/en/stable/getting_started/installation.html)

## Setup 

###### Reddit:

1. While signed in, go to [preferences->apps.](https://www.reddit.com/prefs/apps/)
2. Click "create an app" near the bottom of the screen
3. name: name for your app
4. type: script
5. description: description for your app (optional)
6. about url: (optional)
7. redirect uri: http://localhost:8080
8. Click "create app"
9. Keep track of "client id" and "secret"

###### config.py:
1. username: youre Reddit username
2. password: your Reddit password
3. client_id: client id displayed after clicking "Create app" from step 8. above
4. client_secret: secret id displayed after clicking "Create app" from step 8. above

###### redditbot.py:

Set which subreddit bot will be active in (default = 'test'), will be active in r/test

`a.subreddit('test')`

Set amount of comments bot will scrape through (default = 20)

`a.subreddit('test').comments(limit = 20)`

Set which keyword(s) will activate bot (default = "sample user keyword")

`if "sample user keyword"                                                                                                                                                       `

## Execution

Run the bot in the directory where bot is located

`$ python redditbot.py`






