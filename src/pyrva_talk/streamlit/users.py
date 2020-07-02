from tweepy.error import TweepError
from typing import List
import altair as alt
import numpy as np
import pandas as pd
import streamlit as st

from pyrva_talk.twitter import api
from pyrva_talk.streamlit import url_from_handle, show_chart, select_scale


def users_timeline(data: pd.DataFrame):
    base = (
        alt.Chart(data)
        .mark_circle(size=50)
        .encode(
            x='created_at:T',
            tooltip=['screen_name', 'created_at']
        )
    )
    show_chart(base)


def users_compare(data: pd.DataFrame, field: str):

    scale = alt.Scale(type=select_scale(field))
    base = alt.Chart(data).mark_bar().encode(
        x=alt.X(f'{field}:Q', title='', scale=scale),
        y=alt.Y('screen_name:N', title='', sort='-x')
    )
    show_chart(base)


def display(handles: List[str]) -> None:

    fields = {
        'screen_name': 'Screen Name',
        'name': 'Name',
        'followers_count': 'Followers',
        'friends_count': 'Following',
        'listed_count': 'Listed',
        'created_at': 'Created',
        'favourites_count': 'Favorites',
        'statuses_count': 'Tweets',
    }

    st.title('Compare Users')

    if not handles:
        st.write("Enter handles to compare in sidebar")
    else:
        _users = []
        for handle in handles:
            try:
                _users.append(api.twitter_api.get_user(handle))
            except TweepError:
                continue

        data = pd.DataFrame([
            {
                field: getattr(user, field, None)
                for field in fields.keys()
            }
            for user in _users
        ])

        for u in _users:
            link = url_from_handle(u.screen_name, md_link=True)
            st.sidebar.markdown(
                f'---\n**{link}** {u.name}\n\n{u.description}'
            )

        st.header("Joined Twitter")
        users_timeline(data)

        for col in data.select_dtypes(['int']).columns:
            st.header(fields[col])
            users_compare(data.replace(0, np.nan), col)
