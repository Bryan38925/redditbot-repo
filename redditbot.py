import os.path

import praw
import config
import time
import os
import requests

i = 0

def botLogin():
    a = praw.Reddit(username = config.username,
                password = config.password,
                client_id = config.client_id,
                client_secret = config.client_secret,
                user_agent = "Joke comment responder bot")
    return a #reddit login


def runBot(a):

    for comment in a.subreddit('test').comments(limit = 20):
        if "sample user keyword" in comment.body and comment.id not in repliedTo and comment.author != a.user.me():
            global i
            i += 1

            reply = "Here is the joke:\n\n"
            joke = requests.get("https://api.chucknorris.io/jokes/random").json()['value']
            reply += ">" + joke
            reply += "\n\nThis joke is from [chucknorris.io](https://api.chucknorris.io/)."

            comment.reply(reply)
            print("Replied to " + str(i) + " comment(s)")

            repliedTo.append(comment.id)

            with open("../commentsRepliedTo.txt", "a") as f:
                f.write(comment.id + "\n")

    print("Sleeping for 5 seconds")
    time.sleep(5)

def getSavedComments():
    if not os.path.isfile("../commentsRepliedTo.txt"):
        repliedTo = []
    else:
        with open("../commentsRepliedTo.txt", "r") as f:
            repliedTo = f.read()
            repliedTo = repliedTo.split("\n")
            repliedTo = list(filter(None, repliedTo)) #filter out white space at end of input file

    return repliedTo


a = botLogin()
repliedTo = getSavedComments()

while True:
    runBot(a)
    print(repliedTo)