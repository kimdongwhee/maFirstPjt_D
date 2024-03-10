import streamlit as st
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier

#페이지 제목
st.title("K-Nearest Neighbors(k-최근접이웃)") 
st.markdown('''
            ##### K-최근접 이웃(K-Nearest Neighbors, KNN)은 지도 학습의 한 유형으로, 분류 및 회귀 문제에 사용되는 간단하면서도 강력한 알고리즘으로 주어진 데이터 포인트 주변의 가장 가까운 이웃들을 기반으로 예측을 수행.
            ''')

bream_length = [25.4, 26.3, 26.5, 29.0, 29.0, 29.7, 29.7, 30.0, 30.0, 30.7, 31.0, 31.0, 31.5, 32.0, 32.0, 32.0, 33.0, 33.0, 33.5, 33.5, 34.0, 34.0, 34.5, 35.0, 35.0, 35.0, 35.0, 36.0, 36.0, 37.0, 38.5, 38.5, 39.5, 41.0, 41.0]
bream_weight = [242.0, 290.0, 340.0, 363.0, 430.0, 450.0, 500.0, 390.0, 450.0, 500.0, 475.0, 500.0, 500.0, 340.0, 600.0, 600.0, 700.0, 700.0, 610.0, 650.0, 575.0, 685.0, 620.0, 680.0, 700.0, 725.0, 720.0, 714.0, 850.0, 1000.0, 920.0, 955.0, 925.0, 975.0, 950.0]
smelt_length = [9.8, 10.5, 10.6, 11.0, 11.2, 11.3, 11.8, 11.8, 12.0, 12.2, 12.4, 13.0, 14.3, 15.0]
smelt_weight = [6.7, 7.5, 7.0, 9.7, 9.8, 8.7, 10.0, 9.9, 9.8, 12.2, 13.4, 12.2, 19.7, 19.9]

length = bream_length + smelt_length
weight = bream_weight + smelt_weight

#사이킷런에 돌리기위해 2차원 배열로 생성
fish_array = [[b,s] for b,s in zip(length, weight)]

#지도학습 : 종별로 코드부여 → 정답준비 2진 분류
fish_target = [1]*35 + [0]*14

kn = KNeighborsClassifier()
kn.fit(fish_array, fish_target)
total_score = kn.score(fish_array, fish_target)

#페이지 내용
st.markdown(f'''
            ##### □ 분류를 원하는 신원미상의 물고기 길이와 무게입력(예측정확도 : {total_score})
            ''')

#인풋박스 : 신원미상의 물고기 스팩입력
ipt_length = st.text_input("(1) 길이(숫자만 입력)")
ipt_width = st.text_input("(2) 무게(숫자만 입력)")

if ipt_length and ipt_width != "":
    showChart = plt.figure()
    plt.scatter(bream_length, bream_weight)
    plt.scatter(smelt_length, smelt_weight)
    plt.scatter(float(ipt_length), float(ipt_width), marker='*', c = 'red')
    plt.xlabel("length")
    plt.ylabel("weight")
    st.pyplot(showChart)
else:
    showChart = plt.figure()
    plt.scatter(bream_length, bream_weight)
    plt.scatter(smelt_length, smelt_weight)
    plt.xlabel("length")
    plt.ylabel("weight")
    st.pyplot(showChart)