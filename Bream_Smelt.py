import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

#페이지 제목
st.title("생선분류")

# 공간을 2:2 으로 분할하여 col1과 col2라는 이름을 가진 컬럼을 생성
col1,col2 = st.columns([2,2])
 
#페이지 내용
#도미 데이터
with col1 :
    bream_length = [25.4, 26.3, 26.5, 29.0, 29.0, 29.7, 29.7, 30.0, 30.0, 30.7, 31.0, 31.0, 31.5, 32.0, 32.0, 32.0, 33.0, 33.0, 33.5, 33.5, 34.0, 34.0, 34.5, 35.0, 35.0, 35.0, 35.0, 36.0, 36.0, 37.0, 38.5, 38.5, 39.5, 41.0, 41.0]
    bream_weight = [242.0, 290.0, 340.0, 363.0, 430.0, 450.0, 500.0, 390.0, 450.0, 500.0, 475.0, 500.0, 500.0, 340.0, 600.0, 600.0, 700.0, 700.0, 610.0, 650.0, 575.0, 685.0, 620.0, 680.0, 700.0, 725.0, 720.0, 714.0, 850.0, 1000.0, 920.0, 955.0, 925.0, 975.0, 950.0]

    st.markdown(f'''
                ##### 1.도미 데이터(데이터 {len(bream_length)} 건)
                ''')


    domi_data = pd.DataFrame({
        "길이" : bream_length,
        "무게" : bream_weight
    })
    st.dataframe(domi_data, width=400,height=300)

#빙어 데이터
with col2 : 
    smelt_length = [9.8, 10.5, 10.6, 11.0, 11.2, 11.3, 11.8, 11.8, 12.0, 12.2, 12.4, 13.0, 14.3, 15.0]
    smelt_weight = [6.7, 7.5, 7.0, 9.7, 9.8, 8.7, 10.0, 9.9, 9.8, 12.2, 13.4, 12.2, 19.7, 19.9]

    st.markdown(f'''
                ##### 2.빙어 데이터(데이터 {len(smelt_length)} 건)
                ''')


    domi_data = pd.DataFrame({
        "길이" : smelt_length,
        "너비" : smelt_weight
    })

    st.dataframe(domi_data, width=400,height=300)

#산점도그래프
st.markdown(f'''
            ##### 3.산점도 그래프(도미/빙어)
            ''')

showChart = plt.figure()
plt.scatter(bream_length, bream_weight)
plt.scatter(smelt_length, smelt_weight)
plt.xlabel("length")
plt.ylabel("weight")
st.pyplot(showChart)