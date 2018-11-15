import argparse
import datetime
import json
import os
import requests


class Bot:

    def __init__(self, name=None, url=None, icon=":python:"):
        if name is None:
            self.name = os.uname()[1]
        else:
            self.name = name
        self.icon = icon
        if url is not None:
            self.url = url
        elif os.path.exists(".url"):
            with open(".url", "r") as f:
                self.url = f.readline()

        self.dtformat = "%c"
        self.hostname = os.uname()[1]

    def post_log(self, text):
        dt = datetime.datetime.now()
        text = dt.strftime(self.dtformat) + " : " + text
        self.post(text)

    def post(self, text):
        requests.post(
            self.url,
            data=json.dumps(
                {"text": text,
                 "username": self.name,
                 "icon_emoji": self.icon}))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("name", type=str)
    parser.add_argument("text", type=str)
    parser.add_argument("url", type=str)

    args = parser.parse_args()
    bot = Bot(args.name, args.url)
    bot.post_slack(args.text)
