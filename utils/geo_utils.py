import streamlit as st
from sentinelhub import SHConfig, BBox, CRS, SentinelHubRequest, MimeType, DataCollection, bbox_to_dimensions
import datetime
from PIL import Image
import numpy as np

def display_satellite_view():
    st.subheader("Sentinel-2 Satellite Viewer")

    st.markdown("### 🗝️ Enter SentinelHub API Keys")
    sh_client_id = st.text_input("SentinelHub Client ID", type="password")
    sh_client_secret = st.text_input("SentinelHub Client Secret", type="password")

    if not sh_client_id or not sh_client_secret:
        st.warning("Please enter both SentinelHub Client ID and Secret.")
        return

    config = SHConfig()
    config.sh_client_id = sh_client_id
    config.sh_client_secret = sh_client_secret

    lat = st.number_input("Latitude", value=34.0100)
    lon = st.number_input("Longitude", value=75.3200)
    date = st.date_input("Date", value=datetime.date(2023, 10, 1))
    
    bbox = BBox(bbox=[lon-0.05, lat-0.05, lon+0.05, lat+0.05], crs=CRS.WGS84)
    resolution = 10
    size = bbox_to_dimensions(bbox, resolution=resolution)

    evalscript = """
    return [B04, B03, B02];
    """

    request = SentinelHubRequest(
        data_folder='.',
        evalscript=evalscript,
        input_data=[SentinelHubRequest.input_data(
            data_collection=DataCollection.SENTINEL2_L1C,
            time_interval=(str(date), str(date + datetime.timedelta(days=1)))
        )],
        responses=[SentinelHubRequest.output_response('default', MimeType.PNG)],
        bbox=bbox,
        size=size,
        config=config
    )

    image = request.get_data()[0]
    st.image(image, caption=f"Sentinel-2 Image on {date}", use_column_width=True)

def generate_report():
    st.text_area("Report Notes", "Suspicious movement seen near X coordinates...", height=200)
    if st.button("Export Report"):
        st.success("Report exported (simulation).")
