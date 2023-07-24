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

@st.cache_data()
def func3():
    st.subheader('The Correlation of Wind data')
    st.dataframe(round(data.drop('시간대',axis=1).corr(),2))
func3()

st.subheader('The Scatter plots of Wind data')

v_list=['월','일','섭씨온도','절대온도','이슬점','상대습도','대기압','포화증기압','실제증기압','증기압부족량',
              '수증기함량','공기밀도','풍향','풍속']
vari = st.selectbox(label = "Choose a Variable", options = v_list,key=0)
data=data.sort_values(by=vari).reset_index(drop=True)
a,b = st.select_slider(f'Choose a {vari}.', options=sorted(data[vari]),value=(np.min(sorted(list(set(data[vari])))),np.max(sorted(list(set(data[vari]))))))
k1=list(data[data[vari]==a].index)[0]
k2=list(data[data[vari]==b].index)[-1]

v1_list = list(data.drop('시간대',axis=1).columns)
vari1 = st.selectbox(label = "Choose a First Variable", options = v1_list,key=1)
v2_list = list(data.drop('시간대',axis=1).columns)
vari2 = st.selectbox(label = "Choose a Second Variable", options = v2_list,key=2)
title = f"The scatter plot of {vari1} and {vari2} with Time Zone"
fig1 = px.scatter(data.loc[k1:k2], x=vari1, y=vari2, color='시간대',title=title)
fig1.update_traces(marker={'size':5})
st.plotly_chart(fig1)
