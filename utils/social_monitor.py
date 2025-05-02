import streamlit as st
import requests

def display_social_monitor():
    st.subheader("📡 Twitter (X) Real-Time Monitoring")
    
    keyword = st.text_input("Search keyword", value="explosion OR blackout OR missing")
    lat = 34.0100
    lon = 75.3200
    radius_km = 25
    max_results = 10

    twitter_token = st.text_input("Twitter Bearer Token", type="password")

    if not twitter_token:
        st.warning("Please enter your Twitter Bearer Token to continue.")
        return

    if st.button("Fetch Tweets"):
        st.info("Searching Twitter...")
        headers = {
            "Authorization": f"Bearer {twitter_token}"
        }

        query = f"{keyword} point_radius:[{lon} {lat} {radius_km}km] -is:retweet lang:en"
        url = "https://api.twitter.com/2/tweets/search/recent"
        params = {
            "query": query,
            "max_results": max_results,
            "tweet.fields": "created_at,text,geo",
        }

        response = requests.get(url, headers=headers, params=params)
        if response.status_code == 200:
            data = response.json()
            tweets = data.get("data", [])
            if tweets:
                for tweet in tweets:
                    st.markdown(f"**🕒 {tweet['created_at']}**")
                    st.write(tweet["text"])
                    st.markdown("---")
            else:
                st.warning("No tweets found.")
        else:
            st.error(f"API Error {response.status_code}: {response.text}")
