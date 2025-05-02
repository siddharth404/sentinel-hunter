import streamlit as st
import exifread
import folium
from streamlit_folium import st_folium
from PIL import Image

def get_decimal_from_dms(dms, ref):
    degrees = dms[0].num / dms[0].den
    minutes = dms[1].num / dms[1].den
    seconds = dms[2].num / dms[2].den
    decimal = degrees + (minutes / 60.0) + (seconds / 3600.0)
    if ref in ['S', 'W']:
        decimal = -decimal
    return decimal

def extract_gps_data(tags):
    try:
        lat = get_decimal_from_dms(tags["GPS GPSLatitude"].values, tags["GPS GPSLatitudeRef"].values)
        lon = get_decimal_from_dms(tags["GPS GPSLongitude"].values, tags["GPS GPSLongitudeRef"].values)
        return lat, lon
    except KeyError:
        return None, None

def display_exif_analysis():
    st.subheader("📸 Upload Image for GPS EXIF Analysis")

    uploaded_file = st.file_uploader("Choose an image", type=["jpg", "jpeg"])
    
    if uploaded_file:
        st.image(uploaded_file, use_column_width=True)

        tags = exifread.process_file(uploaded_file)
        gps_data = extract_gps_data(tags)

        if gps_data[0] is not None:
            lat, lon = gps_data
            st.success(f"✅ GPS Found: Latitude: {lat}, Longitude: {lon}")
            
            m = folium.Map(location=[lat, lon], zoom_start=13)
            folium.Marker([lat, lon], popup="📍 Image Location").add_to(m)
            st_folium(m, width=700, height=500)
        else:
            st.warning("⚠️ No GPS data found in image metadata.")
