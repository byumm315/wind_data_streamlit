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

st.subheader('The Histogram of Wind data')
vari1 = st.selectbox(label = "Choose a Variable", options = data.drop(['월','일','시간대'],axis=1).columns,key=1)
fig4 = px.histogram(data,x=vari1,nbins=100)
st.plotly_chart(fig4)
