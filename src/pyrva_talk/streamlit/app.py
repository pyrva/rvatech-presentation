from typing import List, Union
import datetime
import streamlit as st

from pyrva_talk import settings
import pyrva_talk.streamlit.user_detail as user_detail
import pyrva_talk.streamlit.users as users
import pyrva_talk.streamlit.mentions as mentions


USER_DETAIL: str = 'User Detail'
USERS: str = 'Compare Users'
MENTIONS: str = 'Mentions'


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


def main() -> None:
    """Main App Controller."""
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
        user_detail.display(handle)
    elif mode == USERS:
        users.display(handles)
    elif mode == MENTIONS:
        mentions.display(handles, since)


if __name__ == '__main__':
    main()
