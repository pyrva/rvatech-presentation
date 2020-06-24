""" Access to the twitter API """
import datetime as dt
from itertools import chain

import tweepy

from pyrva_talk.twitter.auth import get_auth


auth = get_auth()
twitter_api = tweepy.API(auth)
py_rva = "@PyRVA"


def get_timeline(user=py_rva):
    """ Returns timeline for ``user`` """
    timeline = twitter_api.user_timeline(user)
    return timeline


def get_recent_mentions(user=py_rva, n=5):
    """ Get the ``n`` most recet mentions for ``user`` """
    tweet_cursor = tweepy.Cursor(twitter_api.mentions_timeline, user=user, count=n)
    tweets = [tweet for tweet in chain.from_iterable(tweet_cursor.pages())]
    return tweets


def get_tweets(query=py_rva, start_date=None):
    """ Return tweets for ``query`` (since datetime ``since``)"""

    payload = {
        'q': query
    }
    if start_date:
        payload['since'] = start_date

    # get tweets
    tweet_cursor = tweepy.Cursor(twitter_api.search, **payload)
    tweets = [tweet for tweet in chain.from_iterable(tweet_cursor.pages())]
    
    return tweets
