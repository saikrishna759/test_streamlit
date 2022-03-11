import pandas as pd
import streamlit as st

st.title("Welcome to Streamlit!")

st.write("Our first DataFrame")

st.dataframe(
  pd.read_csv("https://raw.githubusercontent.com/saikrishna759/test_streamlit/main/combined_indian_songs_data.csv")
)
