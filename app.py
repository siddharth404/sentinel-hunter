
import streamlit as st
import random
import datetime
import pandas as pd
import folium
from streamlit_folium import st_folium

st.set_page_config(page_title="Live Threat Tracker", layout="wide")

st.title("🛰️ OSINT + GEOINT Threat Tracker")
st.markdown("Live mock tracking of potential threats using open-source data and satellite view.")

# Mock locations and keywords
locations = {
    "Pahalgam": [33.9986, 75.3250],
    "Pulwama": [33.8740, 74.8990],
    "Anantnag": [33.7312, 75.1486],
    "Srinagar": [34.0837, 74.7973]
}
keywords = ["explosion", "militant", "attack", "gunfire", "encounter", "IED"]

# Simulate live alerts
def generate_alert():
    loc = random.choice(list(locations.keys()))
    keyword = random.choice(keywords)
    time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return {"time": time, "location": loc, "event": keyword, "coords": locations[loc]}

# Display mock alerts
st.subheader("📡 Live Social Media OSINT Alerts")
alerts = [generate_alert() for _ in range(5)]
df_alerts = pd.DataFrame(alerts)
st.dataframe(df_alerts)

# Map view
st.subheader("🗺️ Geo Map")
m = folium.Map(location=[33.85, 75.0], zoom_start=8)
for alert in alerts:
    folium.Marker(
        location=alert["coords"],
        popup=f"{alert['location']}: {alert['event']} ({alert['time']})",
        icon=folium.Icon(color="red", icon="info-sign")
    ).add_to(m)
st_data = st_folium(m, width=1200)
