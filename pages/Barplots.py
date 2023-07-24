import streamlit as st
import plotly.figure_factory as ff
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import numpy as np

data=pd.read_csv('wind_train.csv')
data=data.drop('ID',axis=1)

change_names=['월','일','시간대','섭씨온도','절대온도','이슬점','상대습도','대기압','포화증기압','실제증기압','증기압부족량',
              '수증기함량','공기밀도','풍향','풍속']
for i,j in zip(data.columns,change_names):
    data.rename(columns={i:j},inplace=True)

st.subheader('The Bar plots of Wind data')
v1_list = ['월','일','시간대']
vari1 = st.selectbox(label = "Choose a First Variable", options = v1_list,key=1)
v2_list = ['섭씨온도','절대온도','이슬점','상대습도','대기압','포화증기압','실제증기압','증기압부족량',
              '수증기함량','공기밀도','풍향','풍속']
vari2 = st.selectbox(label = "Choose a Second Variable", options = v2_list,key=2)
title = f"The Bar plot of {vari1} and {vari2}"
fig = px.bar(data, x = vari1, y = vari2,title=title)
st.plotly_chart(fig)
