"""
추가 설치 필요함
pip install streamlit-aggrid
pip show streamlit-aggrid

streamlit run streamlit_korea_aggrid.py

"""

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from st_aggrid import AgGrid, GridOptionsBuilder, ColumnsAutoSizeMode, GridUpdateMode

# 데이터 로드
@st.cache_data
def load_data():
    data = pd.read_csv('data/data_draw_korea.csv')
    if 'Unnamed: 0' in data.columns:
        data.drop('Unnamed: 0', axis=1, inplace=True)
    return data

data = load_data()
plt.rc('font', family="Malgun Gothic")

# Streamlit UI 구성
st.title("🇰🇷 대한민국 광역시도 데이터 분석 (AgGrid)")

# 광역시도 목록
sido_list = data['광역시도'].unique()
sido_name = st.selectbox("조회할 광역시도를 선택하세요", sido_list)

# 데이터 필터링
sido_df = data[data['광역시도'] == sido_name][['행정구역', '인구수', '면적']].reset_index(drop=True)

if sido_df.empty:
    st.error("해당 광역시도의 데이터를 찾을 수 없습니다.")
else:
    # --- AgGrid 설정 ---
    st.subheader(f"📊 {sido_name} 데이터 그리드")
    st.info("💡 열 제목을 클릭하여 정렬하거나, 필터 아이콘을 눌러 데이터를 검색해보세요.")

    gb = GridOptionsBuilder.from_dataframe(sido_df)
    gb.configure_default_column(editable=True, groupable=True, value=True, enableRowGroup=True) # 편집 가능 설정
    gb.configure_pagination(paginationAutoPageSize=False, paginationPageSize=10) # 페이지네이션
    gb.configure_side_bar() # 측면 필터 바 추가
    gb.configure_selection('single') # 행 선택 기능
    grid_options = gb.build()

    # AgGrid 실행
    grid_response = AgGrid(
        sido_df,
        gridOptions=grid_options,
        height=300,
        width='100%',
        update_mode=GridUpdateMode.MODEL_CHANGED,
        columns_auto_size_mode=ColumnsAutoSizeMode.FIT_CONTENTS,
        theme='streamlit' # 또는 'alpine', 'balham', 'material'
    )

    # AgGrid에서 수정한 데이터를 그래프에 반영하기 위해 데이터 가져오기
    updated_df = pd.DataFrame(grid_response['data'])

    # --- 그래프 영역 ---
    col1, col2 = st.columns(2)

    with col1:
        st.subheader(f"👥 인구수 현황")
        fig, ax = plt.subplots(figsize=(10, 8))
        sns.barplot(x='행정구역', y='인구수', data=updated_df.sort_values(by='인구수', ascending=False), ax=ax, palette='viridis')
        plt.xticks(rotation=45)
        st.pyplot(fig)

    with col2:
        st.subheader(f"🗺️ 면적 현황")
        fig, ax = plt.subplots(figsize=(10, 8))
        sns.barplot(x='행정구역', y='면적', data=updated_df.sort_values(by='면적', ascending=False), ax=ax, palette='magma')
        plt.xticks(rotation=45)
        st.pyplot(fig)