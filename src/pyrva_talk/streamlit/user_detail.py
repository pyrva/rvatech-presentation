from tweepy.error import TweepError
import streamlit as st

from pyrva_talk.streamlit import url_from_handle
from pyrva_talk.twitter import api


def display(handle: str) -> None:

    if not handle:
        st.write("Enter Twitter handle for details.")
    else:
        try:
            user = api.twitter_api.get_user(handle)
        except TweepError:
            st.write("That is not a valid handle")
            return

        link = url_from_handle(user.screen_name, md_link=True)
        st.header(f'{link} Details')

        for attr in user.__dir__():
            if attr[0] != '_':
                value = getattr(user, attr)
                st.subheader(attr)
                st.write(value)
