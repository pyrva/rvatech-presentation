from typing import List
import altair as alt
import datetime
import streamlit as st
import pandas as pd

from pyrva_talk.twitter import api
from pyrva_talk.streamlit import show_chart, select_scale


def display(handles: List[str], since: datetime.date) -> None:
    """Render Mentions App."""
    if isinstance(handles, str):
        handles = [handles]

    st.title(f'Comparison of tweets since {since}')

    fields = {
        'created_at': 'created',
        'full_text': 'text',
        'source': 'source',
        'retweet_count': 'retweets',
        'favorite_count': 'favorites',
        'in_reply_to_status_id': 'reply',
        'lang': 'language',
        'id': 'id',
    }

    data = []
    for handle in handles:
        tweets = api.get_tweets(handle[1:], start_date=since)

        for tweet in tweets:
            tweet_data = {
                field: getattr(tweet, field)
                for field in fields.keys()
            }
            tweet_data['user'] = handle
            for entity in ['hashtags', 'symbols', 'user_mentions']:
                tweet_data[entity] = len(getattr(tweet, 'entities')[entity])
            data.append(tweet_data)

    data = pd.DataFrame(data)
    data.rename(columns=fields, inplace=True)
    data['created'] = pd.to_datetime(data.created)
    data['reply_bool'] = ~data.reply.isnull()

    base = alt.Chart(data)

    timeline = base.mark_circle(size=50).encode(
        x=alt.X('created:T', title='Timestamp'),
        y=alt.Y('user:N', title=''),
        color=alt.Color('user:N', legend=None),
        tooltip=['user', 'created']
    ).properties(title='Tweet Timeline')

    sources = base.mark_bar().encode(
        x=alt.X('count():Q', title='Tweets'),
        y=alt.Y('user:N', title=''),
        color='source:N'
    ).properties(title='Tweet Sources')

    languages = base.mark_bar().encode(
        x=alt.X('count():Q', title='Tweets'),
        y=alt.Y('user:N', title=''),
        color='language:N'
    ).properties(title='Tweet Language')

    retweets = base.mark_area(
        opacity=0.3,
        interpolate='step',
    ).encode(
        x=alt.X('hashtags:Q', bin=alt.Bin(maxbins=data.hashtags.max())),
        y=alt.Y('count()', stack=None),
        color=alt.Color('user:N'),
    )

    show_chart(timeline)
    show_chart(sources)
    show_chart(languages)
    show_chart(retweets)

    st.dataframe(data)
