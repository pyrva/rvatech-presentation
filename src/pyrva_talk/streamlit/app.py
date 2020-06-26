from typing import List, Union
import datetime
import streamlit as st
import numpy as np
import pandas as pd
import altair as alt
from tweepy.error import TweepError

from pyrva_talk import settings
from pyrva_talk.twitter import api


USER_DETAIL: str = 'User Detail'
USERS: str = 'Compare Users'
MENTIONS: str = 'Mentions'


def show_chart(graph: alt.Chart):
    st.altair_chart(graph, use_container_width=True)


def select_scale(key: str) -> str:
    scale = 'linear'
    if st.checkbox('Log Axis', key=key):
        scale = 'log'
    return scale


def users_compare(data: pd.DataFrame, field: str):

    scale = alt.Scale(type=select_scale(field))
    base = alt.Chart(data).mark_bar().encode(
        x=alt.X(f'{field}:Q', title='', scale=scale),
        y=alt.Y('screen_name:N', title='', sort='-x')
    )
    show_chart(base)


def url_from_handle(screen_name: str, md_link: bool = False) -> str:
    """Get twitter url from handle as url or markdown link."""
    url = f'https://twitter.com/{screen_name}'
    if md_link:
        return f'[@{screen_name}]({url})'
    else:
        return url


def format_handles(handles: str) -> Union[str, List[str]]:
    """Convert text area input to list of handles with @ prepended."""
    handle_list = handles.replace('\n', ' ').replace(',', ' ').split()
    handle_list = sorted([
        handle if handle[0] == '@' else f'@{handle}'
        for handle in handle_list
    ])

    if len(handle_list) == 0:
        return ''
    elif len(handle_list) == 1:
        return handle_list[0]
    else:
        return handle_list


def user_detail(handle: str) -> None:

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


def users(handles: List[str]) -> None:

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

        for col in data.select_dtypes(['int']).columns:
            st.header(fields[col])
            users_compare(data.replace(0, np.nan), col)


def mentions(handles: List[str], since: datetime.date) -> None:
    st.write(handles)
    st.write(since)


def main() -> None:

    mode = st.sidebar.selectbox("Mode", options=[USER_DETAIL, USERS, MENTIONS])

    handle: str = ''
    if mode in [USER_DETAIL]:
        handle = format_handles(
            st.sidebar.text_input('Twitter Handle')
        )

    handles: List[str] = []
    if mode in [USERS, MENTIONS]:
        handles = format_handles(
            st.sidebar.text_area("Twitter Handles", value='rvatech\nPyRVA')
        )

    since: datetime.date = datetime.datetime.now()
    if mode in [MENTIONS]:
        since = st.sidebar.date_input(
            label="Start Date",
            min_value=(
                    datetime.datetime.now()
                    - datetime.timedelta(days=settings.DATE_SELECT_MAX_HISTORY)
            ),
            max_value=datetime.datetime.now()
        )

    if mode == USER_DETAIL:
        user_detail(handle)
    elif mode == USERS:
        users(handles)
    elif mode == MENTIONS:
        mentions(handles, since)


if __name__ == '__main__':
    main()
