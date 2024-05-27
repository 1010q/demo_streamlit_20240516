import streamlit as st
import pandas as pd
from io import StringIO
import streamlit as st
import numpy as np
import time

def multicolor_picker(label, default_values):
    num_colors = st.sidebar.number_input(label=label, min_value=1, max_value=10, value=len(default_values), step=1)
    colors = []
    for i in range(num_colors):
        color = st.sidebar.color_picker(f'色 {i+1}', value=default_values[i % len(default_values)])
        colors.append(color)
    return colors

st.title('複数の文字色の変更')

text_colors = multicolor_picker('文字色を選択してください', ['#000000', '#FF0000'])

text = "複数の文字色を交互に適用することができるよ！　じゅげむじゅげむごこうのすりきれかいじゃりすいぎょのうんらいまつふうらいまつくうねるところにすむところぱいぽぱいぽみかんぶらじるあめりかかなだるーまにあかしおぺあしんたっくすえらー"
styled_text = ""
for i, char in enumerate(text):
    styled_text += f'<span style="color:{text_colors[i % len(text_colors)]}">{char}</span>'
st.markdown(styled_text, unsafe_allow_html=True)

on = st.toggle("背景をグレーにする")
css = ""
if on:
    st.write("一番好きなお寿司はサーモンかいくらです！")

    image = './pic/green_00080.jpg'

    css = f'''
    <style>
        .stApp {{
            background-image: url({image});
            background-size: cover;
            background-position: center;
            background-color:rgba(255,255,255,0.4);
        }}
        .stApp > header {{
            background-color: transparent;
        }}
    </style>
    '''
    st.markdown(css, unsafe_allow_html=True)
    st.balloons()
else:
    st.snow()

m = "お勉強サイト"
st.title(f':blue[{m}]')

color = st.color_picker("好きな色を選んでね", "#ffffff")
st.write("この色のカラーコードは", color)

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

st.image('./pic/photo-1548407260-da850faa41e3.jpeg', caption='Sunrise by the mountains')
st.write("キレイな風景だね＾＾")


option = st.selectbox(
    "好きなMrs. GREEN APPLEの曲は？",
    ("none","ケセラセラ", "Soranji", "ナハトムジーク","僕のこと"))
if option == "none":
    st.write("曲を選んで！")
else:
    st.write(option,"の歌詞を教えてあげよう")
if option == "ケセラセラ":
    st.link_button("著作権的に直接載せれないからリンク踏んでね！", "https://www.uta-net.com/song/336333/")
elif option == "Soranji":
    st.link_button("著作権的に直接載せれないからリンク踏んでね！", "https://www.uta-net.com/song/326460/")
elif option == "ナハトムジーク":
    st.link_button("著作権的に直接載せれないからリンク踏んでね！", "https://www.uta-net.com/song/348804/")
elif option == "僕のこと":
    st.link_button("著作権的に直接載せれないからリンク踏んでね！", "https://www.uta-net.com/song/260738/")