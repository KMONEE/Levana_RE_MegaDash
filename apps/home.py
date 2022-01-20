import streamlit as st
from PIL import Image

def app():
    levana = Image.open("levana.png")
    st.image(levana)
