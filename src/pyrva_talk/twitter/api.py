""" Access to the twitter API """
import datetime as dt

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
    tweets = twitter_api.mentions_timeline(user, count=n)
    return tweets


def get_tweets_by_hour(query='#PyRVA', num_hours=12):
    """ Count tweets for ``query`` per hour for the last ``num_hours`` hours """
    tweets_by_time = {}

    # put last 12 hours as empty lists in ``tweets_by_time``
    now = dt.datetime.now()
    now = dt.datetime(now.year, now.month, now.day, now.hour)
    for i in range(num_hours):
        time = now - dt.timedelta(hours=i)
        tweets_by_time[time] = []

    # get tweets
    tweets = twitter_api.search(query)

    # bucket tweets
    for tweet in tweets:
        tweet_time = dt.datetime(
            tweet.created_at.year,
            tweet.created_at.month,
            tweet.created_at.day,
            tweet.created_at.hour,
        )
        if tweet_time in tweets_by_time:
            tweets_by_time[tweet_time].append(tweet)
    
    return tweets_by_time
