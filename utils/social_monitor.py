import streamlit as st

def display_social_monitor():
    st.write("Simulated social media post:")
    st.json({"user": "@tourist123", "text": "Weird blackout in Pahalgam area...", "location": "Pahalgam"})
