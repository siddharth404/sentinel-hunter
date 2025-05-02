import streamlit as st
import spacy

@st.cache_resource
def load_model():
    return spacy.load("en_core_web_sm")

nlp = load_model()

def display_nlp_dashboard():
    st.subheader("🧠 NLP Intel from Bulletins / News")

    try:
        sample_text = open("sample_data/bulletins.txt", "r").read()
    except:
        sample_text = "Suspicious white SUV was seen near Pahalgam. Loud explosion reported."

    user_text = st.text_area("Paste Bulletin or News Report", sample_text, height=200)

    if st.button("Extract Intelligence"):
        doc = nlp(user_text)

        persons = [ent.text for ent in doc.ents if ent.label_ == "PERSON"]
        locations = [ent.text for ent in doc.ents if ent.label_ in ["GPE", "LOC"]]
        orgs = [ent.text for ent in doc.ents if ent.label_ == "ORG"]
        vehicles = [token.text for token in doc if token.text.lower() in ["suv", "van", "bike", "truck", "jeep"]]

        st.markdown("### 🕵️ Intelligence Extracted")
        st.json({
            "Persons": list(set(persons)),
            "Locations": list(set(locations)),
            "Organizations": list(set(orgs)),
            "Vehicle Mentions": list(set(vehicles))
        })
