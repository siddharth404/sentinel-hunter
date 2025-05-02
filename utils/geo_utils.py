import streamlit as st
import os
import matplotlib.pyplot as plt

def display_satellite_view():
    st.image("sample_data/satellite_images/sample_satellite.jpg", caption="Sample Satellite View")

def generate_report():
    st.text_area("Report Notes", "Suspicious movement seen near X coordinates...", height=200)
    if st.button("Export Report"):
        st.success("Report exported (simulation).")
