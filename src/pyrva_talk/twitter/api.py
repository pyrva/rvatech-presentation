""" Access to the twitter API """
import tweepy

from pyrva_talk.twitter.auth import get_auth


auth = get_auth()
api = tweepy.API(auth)
py_rva = api.get_user("@PyRVA")


def get_timeline(user=py_rva):
    """ Returns timeline for ``user`` """


def get_tweets_by_hour(user=py_rva, num_hours=12):
    """ Count tweets for ``user`` per hour for the last ``num_hours`` hours """

