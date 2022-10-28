# import streamlit as st
# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt

# st.title("stlite desktop demo app")

# df = pd.DataFrame(
#     np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
#     columns=['lat', 'lon'])

# st.map(df)

# size = st.slider("Sample size", 100, 1000, 100)
# arr = np.random.normal(1, 1, size=size)
# fig, ax = plt.subplots()
# ax.hist(arr, bins=20)

# st.pyplot(fig)

import streamlit as st
from streamlit_option_menu import option_menu
from pgs import config

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