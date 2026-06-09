from deep_translator import GoogleTranslator
import streamlit as st

st.title("Language Translation Tool")
text = st.text_area("Enter text")
source = st.text_input("Source language", "en")
target = st.text_input("Target language", "fr")

if st.button("Translate"):
    translated = GoogleTranslator(source=source, target=target).translate(text)
    st.write(translated)
