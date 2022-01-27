import streamlit as st
from PIL import Image
import requests



def app():

    st.markdown("""## No more scraping! The files are read directly from the server.""")
    st.markdown(f"""## Most recent update: {requests.get('http://165.22.125.123/last_run.txt').text}""")

    
    levana = Image.open("levana.png")
    st.image(levana)
