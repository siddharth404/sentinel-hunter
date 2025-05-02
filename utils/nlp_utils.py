import streamlit as st
import spacy
from spacy.cli import download

# Function to load the model and handle missing model download
@st.cache_resource
def load_model():
    # Check if the model is available, otherwise download it
    try:
        nlp = spacy.load("en_core_web_sm")
    except OSError:
        st.warning("Downloading the English model... This might take a minute.")
        download("en_core_web_sm")
        nlp = spacy.load("en_core_web_sm")
    return nlp

# Load the model
nlp = load_model()

# Function to display the NLP dashboard for intelligence extraction
def display_nlp_dashboard():
    st.subheader("🧠 NLP Intel from Bulletins / News")

    # Try to read sample text or provide default text if the file doesn't exist
    try:
        sample_text = open("sample_data/bulletins.txt", "r").read()
    except:
        sample_text = "Suspicious white SUV was seen near Pahalgam. Loud explosion reported."

    # Allow user to input their own text
    user_text = st.text_area("Paste Bulletin or News Report", sample_text, height=200)

    # When the button is pressed, extract intelligence from the text
    if st.button("Extract Intelligence"):
        doc = nlp(user_text)

        # Extract different types of information
        persons = [ent.text for ent in doc.ents if ent.label_ == "PERSON"]
        locations = [ent.text for ent in doc.ents if ent.label_ in ["GPE", "LOC"]]
        orgs = [ent.text for ent in doc.ents if ent.label_ == "ORG"]
        vehicles = [token.text for token in doc if token.text.lower() in ["suv", "van", "bike", "truck", "jeep"]]

        # Display the extracted information
        st.markdown("### 🕵️ Intelligence Extracted")
        st.json({
            "Persons": list(set(persons)),
            "Locations": list(set(locations)),
            "Organizations": list(set(orgs)),
            "Vehicle Mentions": list(set(vehicles))
        })
