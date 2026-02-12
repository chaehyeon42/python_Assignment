# streamlit run streamlit_uicomponent.py

import streamlit as st
import pandas as pd
import datetime

st.set_page_config(page_title="Streamlit UI 컴포넌트 데모", layout="wide") #set_page_config = 페이지 설정
st.title(" Streamlit UI 컴포넌트 데모") #제목 설정

st.header("1. 텍스트 입력 컴포넌트")
name = st.text_input("이름을 입력하세요:") # text_input = 하나의 text만 입력
bio = st.text_area("자기소개를 입력하세요:") #text_area = 여러 TEXT 입력시 사용하는 기능

st.header("2. 숫자 입력 및 슬라이더")
age = st.number_input("나이 입력", min_value=0, max_value=120, step=1) #number_input => 숫자만 입력 할 수 있는 입력창
score = st.slider("만족도 (0 ~ 100)", 0, 100, 50)

st.header("3. 선택 컴포넌트")
gender = st.radio("성별 선택", ["남성", "여성", "기타"])
job = st.selectbox("직업 선택", ["학생", "직장인", "프리랜서", "기타"])
hobbies = st.multiselect("취미 선택", ["독서", "운동", "여행", "게임", "음악"])

st.header("4. 날짜 및 시간 선택")
today = st.date_input("오늘 날짜 선택", datetime.date.today())
meeting_time = st.time_input("미팅 시간 선택") # time_input = 시간 입력

st.header("5. 체크박스 & 버튼")
agree = st.checkbox("개인정보 수집에 동의합니다.")
if st.button("제출하기"):
    if agree:
        st.success("제출 완료! 감사합니다.")
    else:
        st.warning("동의가 필요합니다.")

st.header("6. 파일 업로드")
uploaded_file = st.file_uploader("CSV 파일 업로드", type="csv")
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.dataframe(df)

st.header("7. 색상 선택기")
color = st.color_picker("좋아하는 색상을 골라보세요", "#00f900")
st.write(f"선택한 색상: {color}")
