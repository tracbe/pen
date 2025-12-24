import sklearn
import joblib
import numpy as np
import pandas as pd
import streamlit as st

model = joblib.load("penguin.pkl")
le = joblib.load('label.pkl')
st.set_page_config(page_title = "penguin type classefier" , page_icon = "🐧")
st.title("Penguin Type Classefier 🐧")

st.sidebar.header("penguin details :")

bill_length_mm = st.sidebar.slider("bill_length_mm :" , 34.1 , 50.6 )
bill_depth_mm = st.sidebar.slider("bill_depth_mm :" , 13.4 , 20.8 )
flipper_length_mm = st.sidebar.slider("flipper_length_mm :" , 170 , 220)
body_mass_g =st.sidebar.slider("body_mass_g :" , 2700, 6700 )

btn = st.button("pred")
if btn :
    input_data = np.array([[bill_length_mm,bill_depth_mm,flipper_length_mm,body_mass_g]] , dtype=np.float32)
    pred = model.predict(input_data) 
    class_list = ['Adelie' , 'Gentoo' , 'Chinstrap']
    if pred == 0 :
        answer = "Adelie"
    if pred == 1 :
        answer = "Gentoo"
    if pred == 2 :
        answer = "Chinstrap" 
    st.success(answer)


