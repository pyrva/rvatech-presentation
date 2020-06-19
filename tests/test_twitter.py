import pytest



def test_twitter_auth():
    """ Ensure API credentials are valid """
    from pyrva_talk.twitter.auth import get_auth
    from tweepy.api import API

    auth = get_auth()
    api = API(auth)
    assert api.verify_credentials()