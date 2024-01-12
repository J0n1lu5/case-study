import streamlit as st
import numpy as np
from streamlit_extras.let_it_rain import rain


genre = st.radio(
    "Pick something",
    ["something special", "powder", "suprise","emoji rain"],
    captions = ["Laugh out loud.", "winter time", "see for yourself","..."])

if genre == 'something special':
    st.image('JNS09797.jpg', caption='ciao rücken')
elif genre =='suprise':
    st.balloons()
elif genre == 'powder':
    st.snow()
elif genre == 'emoji rain':
    rain(
        emoji="🌧️",
        font_size=156,
        falling_speed=7,
        animation_length="infinite",
    )

color = st.color_picker('Pick A Color', '#00f900')
st.write('The current color is', color)