import streamlit as st

st.title("Hello, Streamlit")

name = st.text_input("Username", placeholder="Set Username")
password = st.text_input("Password", type="password")

login = st.button("Log In")
if login:
    
    st.write("THANK YOU FOR LOGIN")
register = st.button("Register")
if register:
    st.switch_page("pages/register.py")