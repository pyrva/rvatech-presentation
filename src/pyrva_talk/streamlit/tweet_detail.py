from tweepy.error import TweepError
import streamlit as st

from pyrva_talk.twitter import api
from pyrva_talk.streamlit import url_from_handle


def display(handle: str) -> None:
    """Render Tweet Detail App."""
    if not handle:
        st.write("Enter Twitter handle for details.")
    else:
        try:
            user = api.twitter_api.get_user(handle)
        except TweepError:
            st.write("That is not a valid handle")
            return

        link = url_from_handle(user.screen_name, md_link=True)
        most_recent = user.timeline()[0]
        start_date = getattr(most_recent, 'created_at').strftime('%Y-%m-%d')
        st.header(f"{link}'s Last Tweet: {start_date}")

        tweet = api.get_tweets(user.screen_name, start_date=start_date)[0]

        for attr in tweet.__dir__():
            if attr[0] != '_':
                st.subheader(attr)
                st.write(getattr(tweet, attr))

