// threat_intel_dashboard/app.py

import streamlit as st
import requests
import pandas as pd

st.set_page_config(page_title="Threat Intel Dashboard", layout="wide")

st.title("🛰️ Threat Intel Dashboard")

st.sidebar.header("🔐 API Keys Configuration")
twitter_api_key = st.sidebar.text_input("Twitter/X Bearer Token", type="password")
sentinel_instance_id = st.sidebar.text_input("Sentinel Hub Instance ID")
sentinel_client_id = st.sidebar.text_input("Sentinel Hub Client ID")
sentinel_client_secret = st.sidebar.text_input("Sentinel Hub Client Secret", type="password")

st.sidebar.header("📍 Inputs")
keyword = st.sidebar.text_input("Search Keyword", "terrorism")
location = st.sidebar.text_input("Location Filter (optional)", "")

st.write("### 🌐 Twitter/X Keyword Search")
if twitter_api_key:
    headers = { "Authorization": f"Bearer {twitter_api_key}" }
    query = keyword
    url = f"https://api.twitter.com/2/tweets/search/recent?query={query}&max_results=10&tweet.fields=created_at,text"
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        tweets = response.json().get("data", [])
        for tweet in tweets:
            st.write(f"🕒 {tweet['created_at']}")
            st.write(f"💬 {tweet['text']}")
            st.markdown("---")
    else:
        st.error("Failed to fetch tweets. Check your API key.")
else:
    st.warning("Enter your Twitter/X API key to fetch tweets.")

st.write("### 🛰️ Satellite Imagery (Placeholder)")
st.info("Sentinel Hub integration not activated in this prototype. Add logic with Sentinel Hub APIs here.")
