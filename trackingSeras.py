import tweepy
import logging
from api import create_api
from datetime import datetime
import random
logging.basicConfig(filename="relatorioDeMerdas.log", level=logging.INFO)
logger = logging.getLogger()
tweetId = ""
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
dependes = [
    "depende...",
    "Depende...",
    "depende",
    "hm... depende",
    "Hmmmm... depende...",
    "como sempre, depende",
    "pelo visto, depende.",
    "preciso analisar a complexidade, então depende",
    "preciso analisar a complexidade, então depende.",
    "esse cenário depende de muitas questões",
    "esse cenário depende de muitas questões.",
    "Já tentou fazer isso com javascript?",
    "Sempre dependenderá da complexidade. Então, depende",
    "Depende de muitos dependes",
    "Existem muitos dependes para analisar."

]


class RetweetListener(tweepy.StreamListener):
    def __init__(self, api):
        self.api = api
        self.me = api.me()

    def on_status(self, tweet):
        index = random.randint(0, len(dependes))
        processing = 'Processando tweet - {}'.format(tweet.text)
        msg = logger.info(processing)
        tweetId = tweet.id
        if msg != None:
            print(msg)
        if tweet.is_quote_status == False & tweet.favorited == False & tweet.retweeted == False:
            try:

                tweet.favorite()
                api.update_status(
                    status=dependes[index], in_reply_to_status_id=tweetId, auto_populate_reply_metadata=True)
                logger.info({
                    "Status": "OK",
                    "Tweet ID": tweetId,
                    "Link": f"https://twitter.com/twitter/status/{tweetId}"
                })
                print(str({
                    "Status": "OK",
                    "Tweet ID": tweetId,
                    "Link": f"https://twitter.com/twitter/status/{tweetId}"
                }))
            except tweepy.error.TweepError as error:

                print(str({
                    "Status": "Warning",
                    "Tweet ID": tweetId,
                    "Link": f"https://twitter.com/twitter/status/{tweetId}",
                    "Error": str(error)
                }))
                logger.error({
                    "Status": "Warning",
                    "Tweet ID": tweetId,
                    "Link": f"https://twitter.com/twitter/status/{tweetId}",
                    "Error": str(error)
                })
                pass

    def on_error(self, status):
        print(status.text)

        logger.error(status)
        if status == 420:
            return False


api = create_api()
tweets_listener = RetweetListener(api)
while True:
    try:
        stream = tweepy.Stream(auth=api.auth, listener=tweets_listener)
        stream.filter(track=['cc: @sseraphini', 'cc:@sseraphini', 'cc @sseraphini',
                      'Cc @sseraphini', 'Cc: @sseraphini', 'Cc:@sseraphini'])
    except Exception as error:
        print(str({
            "Status": "Critical",
            "Tweet ID": tweetId,
            "Link": f"https://twitter.com/twitter/status/{tweetId}",
            "Error": str(error)
        }))
        logger.error({
            "Status": "Critical",
            "Tweet ID": tweetId,
            "Link": f"https://twitter.com/twitter/status/{tweetId}",
            "Error": str(error)
        })
        pass
