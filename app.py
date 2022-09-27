import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image, ImageSequence


st.title('Sidabari Project ')

st.write('# Gender')

man_woman = st.slider('gender', 0, 60, 30)
# filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]

def open_img(sexibility):
    img_path = f'gender/frame{"%0.2d" %sexibility}.png'
    img = Image.open(img_path)
    return img

st.image(open_img(man_woman+20))

st.subheader(f'Gender of the One: {"%0.3f" %(man_woman/60 * 100)} % Man')

#------------------------------------------------------------------------------------

st.write('# Season')

option = st.selectbox(
    'Sellect Option',
    ('Woman 1', 'Woman 2', 'Man 1', 'Man 2'))

st.write('Seasonal look of :', option)


man_woman = st.slider('Seasonal', 0, 90 , 45)
# filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]
dict_opt = {'Woman 1' : 1046 , 'Woman 2': 3672 , 'Man 1': 1771 , 'Man 2':14369} #dict for selectbar option
def open_img_sl(sexibility,opt):
    img_path = f'season/{dict_opt[opt]}/{dict_opt[opt]}_{"%03d" %sexibility}.jpeg'
    img = Image.open(img_path)
    return img
st.image(open_img_sl(man_woman+29,option))
# st.image(frames[man_woman])

st.subheader(f'Seasonal : {"%0.3f" %(man_woman/90 * 100)} % Summer')