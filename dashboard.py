import streamlit as st
import pandas as pd

metrics = pd.read_csv("data/metrics.csv")

st.title("AI Bot Engagement Metrics")
st.metric("Questions Asked", metrics.at[0,'questions_asked'])
st.metric("Questions Answered", metrics.at[0,'questions_answered'])
st.metric("Tickets Created", metrics.at[0,'tickets_created'])
