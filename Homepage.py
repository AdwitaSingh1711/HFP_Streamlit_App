import streamlit as st

#for importing animations
import json
import requests
from streamlit_lottie import st_lottie

#https://github.com/andfanilo/streamlit-lottie

st.set_page_config(
    page_title="Crop Recommendation",
    page_icon="🌾",
    layout="wide",
)

st.sidebar.success("Select a page above.")

def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

def load_lottieurl(url:str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


#---LOAD ASSETS -----

lottie_hello = load_lottieurl("https://lottie.host/a1a6ec1c-74c9-4e5b-b2e7-eab50a4e0dba/3YmX68QRAw.json")

lottie_mail = load_lottieurl("https://lottie.host/1507e74f-64f5-4174-95f8-62560addeb91/4HPC1ZWm3c.json")

# Header
with st.container():
    st.header("Not sure if your heart is retirement ready?")
    left_column, right_column = st.columns(2)

    with left_column:
        st.write('##')
        st.write("""
                 According to World Health Organization, Cardiovascular diseases (CVDs) are the leading cause of death globally, taking an estimated 17.9 million lives each year.
                 """)
        st.write("Start your journey towards a healthier heart with:")
        st.title("Heart Health")
        st.write(""" 
                 Head towards the Prediction Section to try out our heart failure prediction algorithm!
                 
                 P.S: It is completely free :)
                 """)
    
    with right_column:
        st.lottie(lottie_hello, height=370, key="heart")

