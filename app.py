import streamlit as st
import pyshorteners as pyst
import pyperclip

shortner = pyst.Shortener()

def copying():
    pyperclip.copy(shortner_url)

st.markdown("<h1 style='text-align: center; margin: 1rem 0;'> Url Shortner </h1>", unsafe_allow_html=True)
# st.markdown("---")

form = st.form("name")
url = form.text_input("URL HERE")
s_btn = form.form_submit_button("SHORT")

if s_btn: 
    shortner_url = shortner.tinyurl.short(url)
    st.markdown("<h3> Shorted URL </h3>", unsafe_allow_html=True)
    st.markdown(f"<h6 style='text-align: center;'> {shortner_url} </h6>", unsafe_allow_html=True)
    st.button("Copy", on_click=copying)
