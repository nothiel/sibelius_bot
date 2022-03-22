import tweepy
# from tweet import tweet
from api import create_api
api = create_api()


# função para deletar todos os tweets da conta, para casos extremos de bug
# não utilizado desde o dia 22/03/2022, as 12h e pouca
def deleteAll():
    timeline = tweepy.Cursor(api.user_timeline).items()
    for tweet in timeline:
        api.destroy_status(tweet.id)


deleteAll()
