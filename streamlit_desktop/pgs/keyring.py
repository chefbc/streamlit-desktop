import streamlit as st
import os

def show():
    st.header(os.path.basename(__file__).split(".")[0].capitalize())

    st.write("DB username:", st.secrets["db_username"])
    st.write("DB password:", st.secrets["db_password"])
    st.write("My cool secrets:", st.secrets["my_cool_secrets"]["things_i_like"])