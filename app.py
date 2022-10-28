import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_desktop.pages import config

VERSION = ".".join(st.__version__.split(".")[:2])

def main():

    with st.sidebar:
        page = option_menu(
            None,
            list(config.PAGES.keys()),
            icons=[v["icon"] for k, v in config.PAGES.items()],
            menu_icon="cast",
            default_index=0,
        )

        st.write(f"Made with Streamlit {VERSION}!")

    # select the page based on menu
    if page in config.PAGES:
        config.PAGES[page]["method"]()


if __name__ == "__main__":
    main()