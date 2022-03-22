import tweepy
import logging
from os import getenv

logger = logging.getLogger("SibeliusBot")


def create_api():

    auth = tweepy.OAuthHandler(getenv('CONSUMER_KEY'), getenv('CONSUMER_SECRET'))
    auth.set_access_token(getenv('ACCESS_TOKEN'), getenv('ACCESS_TOKEN_SECRET'))
    api = tweepy.API(auth, wait_on_rate_limit=True,
                     wait_on_rate_limit_notify=True)
    try:
        api.verify_credentials()
    except Exception as e:
        logger.error("Erro criando a API", exc_info=True)
        raise e
    print("API CRIADA")
    logger.info("API criada")
    return api
