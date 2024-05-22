import streamlit as st
import pandas as pd
from io import StringIO
import streamlit as st
import numpy as np
import time

st.title(':blue[お勉強サイト]')

st.header('')

st.write("Hello world😇","*Hello world*")

st.text('ITの勉強がしたいなら')
st.link_button("ここで勉強しよう", "https://www.ap-siken.com/apkakomon.php")

df = pd.DataFrame(
    np.random.randn(10, 2) / [50, 50] + [34.7, 135.24],
    columns=['lat', 'lon'])

st.map(df)


_LOREM_IPSUM = """
Lorem ipsum dolor sit amet, **consectetur adipiscing** elit, sed do eiusmod tempor
incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis
nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
"""

def stream_data():
    for word in _LOREM_IPSUM.split(" "):
        yield word + " "
        time.sleep(0.02)

    yield pd.DataFrame(
        np.random.randn(5, 10),
        columns=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"],
    )

    for word in _LOREM_IPSUM.split(" "):
        yield word + " "
        time.sleep(0.02)


if st.button("Stream data"):
    st.write_stream(stream_data)

st.image('/Users/youta/demo_streamlit_20240516/photo-1548407260-da850faa41e3.jpeg', caption='Sunrise by the mountains')
st.write("キレイな風景だね＾＾")