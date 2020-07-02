from typing import List
import datetime
import streamlit as st


def display(handles: List[str], since: datetime.date) -> None:
    """Render Mentions App."""
    st.write(handles)
    st.write(since)
