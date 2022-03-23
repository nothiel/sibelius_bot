import tweepy
import logging
from api import create_api
import random
logging.basicConfig(filename="relatorioDeMerdas.log", level=logging.INFO)
logger = logging.getLogger('SibeliusBot')

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
    "Existem muitos dependes para analisar.",
    "depends",
    "maybe",
    "depends on the complexity",
    "i need to analyse better, so it depends",
    "too many variables, depends",
    "depends on your approach",
    "as always, depends.",
    "have you tried with javascript?",
    "depends on a lot of maybes"
]


class RetweetListener(tweepy.StreamListener):
    def __init__(self, api):
        self.api = api
        self.me = api.me()
        self.tweet_id = ''

    def on_status(self, tweet):
        processing = f'Processando tweet - {tweet.text}'
        msg = logger.info(processing)
        self.tweet_id = tweet.id
        if msg:
            print(msg)
        if tweet.is_quote_status == False & tweet.favorited == False:
            # aqui existe um bug... Se alguem retuitar um tweet que o bot ja curtiu/comentou, ele passa por essa verificação.
            # não chega a quebrar o app, só registra no log com warning. logo mais descubro como resolver
            try:

                tweet.favorite()
                api.update_status(
                    status=random.choice(dependes), in_reply_to_status_id=self.tweet_id, auto_populate_reply_metadata=True)
                logger.info({
                    "Status": "OK",
                    "Tweet ID": self.tweet_id,
                    "Link": f"https://twitter.com/twitter/status/{self.tweet_id}"
                })
                print(str({
                    "Status": "OK",
                    "Tweet ID": self.tweet_id,
                    "Link": f"https://twitter.com/twitter/status/{self.tweet_id}"
                }))
            except tweepy.error.TweepError as error:

                print(str({
                    "Status": "Warning",
                    "Tweet ID": self.tweet_id,
                    "Link": f"https://twitter.com/twitter/status/{self.tweet_id}",
                    "Error": str(error)
                }))
                logger.error({
                    "Status": "Warning",
                    "Tweet ID": self.tweet_id,
                    "Link": f"https://twitter.com/twitter/status/{self.tweet_id}",
                    "Error": str(error)
                })
                pass

    def on_error(self, status):
        print(status.text)

        logger.error(status)
        if status == 420:
            return False


if __name__ == '__main__':
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
                "Tweet ID": tweets_listener.tweet_id,
                "Link": f"https://twitter.com/twitter/status/{tweets_listener.tweet_id}",
                "Error": str(error)
            }))
            logger.error({
                "Status": "Critical",
                "Tweet ID": tweets_listener.tweet_id,
                "Link": f"https://twitter.com/twitter/status/{tweets_listener.tweet_id}",
                "Error": str(error)
            })
            pass
