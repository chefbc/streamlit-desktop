import os
from io import StringIO

import streamlit as st


def show():
    st.header(os.path.basename(__file__).split(".")[0].capitalize())

    uploaded_file = st.file_uploader("Choose a file", type=["json"])
    if uploaded_file is not None:

        # To convert to a string based IO:
        stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))

        # To read file as string:
        string_data = stringio.read()
        st.write(string_data)
