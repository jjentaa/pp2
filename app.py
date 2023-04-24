import streamlit as st
import pandas as pd
import numpy as np
#import matplotlib.pyplot as plt
from  PIL import Image, ImageEnhance

st.title('Determination chloride in Groundwater using images from test kits')

up_img = st.file_uploader("Upload image (limit 200 MB)", type=['jpg','png','jpeg'])
if up_img is not None:
    image = Image.open(up_img)
    st.image(image, width=300)

    #convert
    img = np.array(image.convert('RGB'))
    h, w = len(img), len(img[0])
    mid_x, mid_y = int(h/2), int(w/2)

    #g color
    x = img[mid_x][mid_y][1]

    
    #y=0.1056*x+86.39
    y = (x-86.39)/0.1056

    if(x<118.3):
        status="normal"
        st.markdown("**<span style='color:rgba(101, 246, 142, 1)'>Normal</span>**", unsafe_allow_html=True)
    elif(x>138.67):
        status="high"
        st.markdown("**<span style='color:rgbargba(200, 0, 0, 1)'>High</span>**", unsafe_allow_html=True)
        st.write(f"concentation : {int(y)} ppm")
    
    else:
        if(y<191): 
            status="normal"
            st.markdown("**<span style='color:rgba(101, 246, 142, 1)'>Normal</span>**", unsafe_allow_html=True)

        elif(y<=250): 
            status="normal"
            st.markdown("**<span style='color:rgbargba(101, 246, 142, 1)'>Normal/span>**", unsafe_allow_html=True)
            st.write(f"concentation : {int(y)} ppm")
        
        elif(y<=303): 
            status="high"
            st.markdown("**<span style='color:rgbargba(246, 101, 101, 1)'>High</span>**", unsafe_allow_html=True)
            st.write(f"concentation : {int(y)} ppm")

        else: 
            status="high"
            st.markdown("**<span style='color:rgba(246, 240, 101, 1)'>High</span>**", unsafe_allow_html=True)

    # txt = st.text_area("", status)
    #st.write(txt)

    # print("x=", x)
    # print("y=", y)

    #print(img.shape)
    #print(np.unique(img//85*85))
