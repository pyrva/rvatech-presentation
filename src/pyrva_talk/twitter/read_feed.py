""" Tools for reading tweets from a twitter feed """

import tweepy

from pyrva_talk import settings


auth = tweepy.OAuthHandler(settings.TWITTER_API_KEY, settings.TWITTER_API_SECRET_KEY, settings.TWITTER_API_CALLBACK_URL)