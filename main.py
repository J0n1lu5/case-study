import streamlit as st
import numpy as np
from streamlit_extras.let_it_rain import rain



st.title('mock up ui')

tab1, tab2 = st.tabs(["Gerät anlegen", "Gerät reservieren"])

with tab1:
    name = st.text_input('Gerätename', '3d Drucker')
    operator = st.text_input('Verantwortlicher', 'Max Mustermann')
    maintenance = st.text_input('Wartungszeitraum', '3 Monate')
    
    st.write('Das Gerät', name, 'von' , operator, 'muss alle' , maintenance, 'gewartet werden')






















"""
erste tests
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
"""
