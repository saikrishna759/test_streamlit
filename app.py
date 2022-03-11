import pandas as pd
import streamlit as st

st.title("Welcome to Streamlit!")

st.write("Our first DataFram")

st.dataframe(
  pd.read_csv("https://github.com/saikrishna759/test_streamlit/blob/main/combined_indian_songs_data.csv")
)
