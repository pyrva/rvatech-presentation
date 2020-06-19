import pytest

from pyrva_talk import twitter


def test_twitter_auth():
    auth = twitter.read_feed.auth