import altair as alt
import streamlit as st


def url_from_handle(screen_name: str, md_link: bool = False) -> str:
    """Get twitter url from handle as url or markdown link."""
    url = f'https://twitter.com/{screen_name}'
    if md_link:
        return f'[@{screen_name}]({url})'
    else:
        return url


def show_chart(graph: alt.Chart):
    st.altair_chart(graph, use_container_width=True)


def select_scale(key: str) -> str:
    scale = 'linear'
    if st.checkbox('Log Axis', key=key):
        scale = 'log'
    return scale
