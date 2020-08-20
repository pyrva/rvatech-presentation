""" Twitter authorization """

import tweepy

from pyrva_talk import settings


def get_auth():
    """ Authenticates with Twitter based on settings in ``settings`` """
    auth = tweepy.OAuthHandler(
        settings.TWITTER_API_KEY,
        settings.TWITTER_API_SECRET_KEY,
        settings.TWITTER_API_CALLBACK_URL,
    )
    auth.set_access_token(settings.TWITTER_API_ACCESS_KEY, settings.TWITTER_API_ACCESS_SECRET)
    return auth