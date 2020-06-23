import altair as alt
import pandas as pd
import streamlit as st
from pyrva_talk.twitter import api

handle = st.sidebar.text_input("Twitter Handle", value='ThePSF')
hours = st.sidebar.slider("Days", min_value=1, max_value=48, value=12, step=1)

if handle and handle[0] != '@':
    handle = '@' + handle

st.title(f'{handle} Twitter Data')

if not handle:
    st.write("Enter handle in sidebar")
else:
    response = api.get_tweets_by_hour(handle, hours)

    data = pd.DataFrame([(i, len(response[i])) for i in response], columns=['hour', 'tweets'])

    st.altair_chart(
        alt.Chart(data).mark_bar().encode(
            x='hour:T', y='tweets'
        ),
        use_container_width=True
    )

    for i in response:
        if len(response[i]):
            st.header(i)
            for tweet in response[i]:
                # st.write(tweet._json)
                st.subheader(f"@{tweet._json['user']['screen_name']}")
                st.markdown(f"{tweet._json['text']}")
