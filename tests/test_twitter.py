import datetime as dt

import pytest


def test_twitter_auth():
    """ Ensure API credentials are valid """
    from pyrva_talk.twitter.auth import get_auth
    from tweepy.api import API

    auth = get_auth()
    api = API(auth)
    assert api.verify_credentials()


def test_get_timeline():
    from pyrva_talk.twitter.api import get_timeline

    tweets = get_timeline()

    assert isinstance(tweets, list)


def test_get_recent_mentions():
    from pyrva_talk.twitter.api import get_recent_mentions

    tweets = get_recent_mentions()

    assert isinstance(tweets, list)


def test_get_tweets():
    from pyrva_talk.twitter.api import get_tweets

    tweets = get_tweets()
    assert isinstance(tweets, list)


def test_get_tweets_since_yesterday():
    from pyrva_talk.twitter.api import get_tweets

    yesterday = dt.datetime.now() - dt.timedelta(days=1)
    tweets = get_tweets(start_date=yesterday.strftime("%x"))
    assert isinstance(tweets, list)
