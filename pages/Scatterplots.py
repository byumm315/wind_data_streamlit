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

st.subheader('The Scatter plots of Wind data')
@st.cache_data()
def func3():
    fig2 = px.scatter_matrix(data.drop('시간대',axis=1))
    fig2.update_traces(marker={'size':3})
    st.plotly_chart(fig2)
    st.subheader('The Correlation of Wind data')
    st.dataframe(round(data.drop('시간대',axis=1).corr(),2))
func3()

v1_list = list((data.drop('시간대',axis=1).columns)
vari1 = st.selectbox(label = "Choose a First Variable", options = v1_list,key=1)
v2_list = list((data.drop('시간대',axis=1).columns)
vari2 = st.selectbox(label = "Choose a Second Variable", options = v2_list,key=2)
title = f"The scatter plot of {vari1} and {vari2} with Time Zone"
fig1 = px.scatter(data, x=vari1, y=vari2, color='시간대',title=title)
fig1.update_traces(marker={'size':5})
st.plotly_chart(fig1)
