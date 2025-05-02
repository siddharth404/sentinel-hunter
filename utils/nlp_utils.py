import streamlit as st

def display_nlp_dashboard():
    st.write("Named Entities:")
    st.json({"Suspect": "Unknown Male", "Vehicle": "White SUV", "Location": "Pahalgam"})
