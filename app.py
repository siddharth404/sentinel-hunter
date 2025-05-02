import streamlit as st
from utils import geo_utils, nlp_utils, exif_utils, social_monitor

st.set_page_config(page_title="OSINT Geospatial Tracker", layout="wide")

st.title("🛰️ OSINT Geospatial & Social Tracker - Pahalgam")

tab1, tab2, tab3, tab4, tab5 = st.tabs(["Satellite & Map", "Social Media", "EXIF", "NLP Intel", "Report"])

with tab1:
    st.header("🗺️ Satellite and Terrain Data")
    geo_utils.display_satellite_view()

with tab2:
    st.header("📱 Social Media Monitor")
    social_monitor.display_social_monitor()

with tab3:
    st.header("📸 EXIF GPS Analyzer")
    exif_utils.display_exif_analysis()

with tab4:
    st.header("🧠 NLP on News & Bulletins")
    nlp_utils.display_nlp_dashboard()

with tab5:
    st.header("📝 Final Report")
    geo_utils.generate_report()
