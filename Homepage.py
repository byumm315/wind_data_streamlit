import streamlit as st
import plotly.figure_factory as ff
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import numpy as np
st.set_page_config(
    page_title="Home"
)
st.title('Wind Speed Predictor') #홈페이지 제목추가
st.header('Wind Data')
st.image('https://images.nationalgeographic.org/image/upload/t_edhub_resource_key_image/v1652340973/EducationHub/photos/wind-farm.jpg')
diamond_df=pd.read_csv('wind_train.csv')
diamond_df=diamond_df.drop('Unnamed: 0',axis=1) #Unnamed: 0 변수 삭제하기
diamond_df=diamond_df.drop(diamond_df[(diamond_df["x"]==0)|(diamond_df["y"]==0)|(diamond_df["z"]==0)].index).reset_index(drop=True) #x, y, z 셋 중 하나라도 0인 행은 삭제하였다.
st.write(diamond_df.head(20))
