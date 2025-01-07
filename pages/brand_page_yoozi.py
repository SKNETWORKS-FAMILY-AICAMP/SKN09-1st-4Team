import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np

# 1. 데이터 불러오기
@st.cache_data
def load_data():
    data = pd.DataFrame({
        "브랜드": [
            "현대", "현대", "현대", "현대", "현대", "현대", "현대", "현대",
            "기아", "기아", "기아", "기아", "기아", "기아", "기아", "기아",
            "제네시스", "제네시스", "제네시스"
        ],
        "기종": [
            "2025 캐스퍼 일렉트릭", "2024 아이오닉 5", "2025 아이오닉 5 N", "2025 ST1",
            "2024 포터2 일렉트릭", "2024 아이오닉 6", "2024 넥쏘", "2024 코나 일렉트릭",
            "2025 봉고3 EV", "2025 EV3", "2025 EV6 GT", "2025 EV9",
            "2025 레이 EV", "2025 니로 EV", "2025 EV6", "2024 니로 플러스",
            "2025 일렉트리파이드 G80", "2024 GV60", "2024 일렉트리파이드 GV70"
        ],
        "가격(만원)": [
            "2740~2990", "4700~6242", "7700", "5595~7195",
            "4395~4554", "4695~6182", "6950", "4142~5086",
            "4315~4550", "3995~4850", "7220", "7337~8397",
            "2735~2955", "4855~5120", "5260~6242", "4755~4850",
            "8490", "6433~7343", "7332"
        ],
        "연비(km/kWh)": [
            "5.6~5.8", "4.4~5.2", "3.7", "3.3~3.8",
            "3.1", "5.5~6.2", "96.2", "4.7~5.5",
            "3.1", "5.1~5.4", "3.8", "3.8~4.2",
            "5.1", "5.3", "4.9~5.2", "5.3",
            "4.4", "4.1~5.1", "4.6"
        ],
        "출시년도": [
            2025, 2024, 2025, 2025,
            2024, 2024, 2024, 2024,
            2025, 2025, 2025, 2025,
            2025, 2025, 2025, 2024,
            2025, 2024, 2024
        ],
        "보러가기": [
            "https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&mra=bjg1&pkid=128&os=34368482&qvt=0&query=2025%20%EC%BA%90%EC%8A%A4%ED%8D%BC%20%EC%9D%BC%EB%A0%89%ED%8A%B8%EB%A6%AD",
            "https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&mra=bjg1&pkid=128&os=33738249&qvt=0&query=2024%20%EC%95%84%EC%9D%B4%EC%98%A4%EB%8B%89%205",
            "https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&mra=bjg1&pkid=128&os=35245739&qvt=0&query=2025%20%EC%95%84%EC%9D%B4%EC%98%A4%EB%8B%89%205%20N",
            "https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&mra=bjg1&pkid=128&os=35250257&qvt=0&query=2025%20ST1",
            "https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&mra=bjg1&pkid=128&os=33624680&qvt=0&query=2024%20%ED%8F%AC%ED%84%B02%20%EC%9D%BC%EB%A0%89%ED%8A%B8%EB%A6%AD",
            "https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&mra=bjg1&pkid=128&os=32106942&qvt=0&query=2024%20%EC%95%84%EC%9D%B4%EC%98%A4%EB%8B%89%206",
            "https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&mra=bjg1&pkid=128&os=31684020&qvt=0&query=2024%20%EB%84%A5%EC%8F%98",
            "https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&mra=bjg1&pkid=128&os=33738233&qvt=0&query=2024%20%EC%BD%94%EB%82%98%20%EC%9D%BC%EB%A0%89%ED%8A%B8%EB%A6%AD",
            "https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&mra=bjg1&pkid=128&os=36332095&qvt=0&query=2025%20%EB%B4%89%EA%B3%A03%20EV",
            "https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&mra=bjg1&pkid=128&os=34212257&qvt=0&query=2025%20EV3",
            "https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&mra=bjg1&pkid=128&os=35994797&qvt=0&query=2025%20EV6%20GT",
            "https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&mra=bjg1&pkid=128&os=35107781&qvt=0&query=2025%20EV9",
            "https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&mra=bjg1&pkid=128&os=35360929&qvt=0&query=2025%20%EB%A0%88%EC%9D%B4%20EV",
            "https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&mra=bjg1&pkid=128&os=35083038&qvt=0&query=2025%20%EB%8B%88%EB%A1%9C%20EV",
            "https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&mra=bjg1&pkid=128&os=34072629&qvt=0&query=2025%20EV6",
            "https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&mra=bjg1&pkid=128&os=29747546&qvt=0&query=2024%20%EB%8B%88%EB%A1%9C%20%ED%94%8C%EB%9F%AC%EC%8A%A4",
            "https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&mra=bjg1&pkid=128&os=34368476&qvt=0&query=2025%20%EC%9D%BC%EB%A0%89%ED%8A%B8%EB%A6%AC%ED%8C%8C%EC%9D%B4%EB%93%9C%20G80",
            "https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&mra=bjg1&pkid=128&os=33761086&qvt=0&query=2024%20GV60",
            "https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&mra=bjg1&pkid=128&os=31951493&qvt=0&query=2024%20%EC%9D%BC%EB%A0%89%ED%8A%B8%EB%A6%AC%ED%8C%8C%EC%9D%B4%EB%93%9C%20GV70"
        ]
    })
    
    # 가격과 연비의 중간값 계산을 위한 새로운 컬럼 추가
    def extract_mean_value(x):
        if '~' in str(x):
            values = [float(v) for v in x.split('~')]
            return np.mean(values)
        return float(x)
    
    data['평균가격'] = data['가격(만원)'].apply(extract_mean_value)
    data['평균연비'] = data['연비(km/kWh)'].apply(lambda x: extract_mean_value(x) if x != '96.2' else None)
    
    return data

# 2. 페이지 설정
st.set_page_config(layout="wide", page_title="국내 전기차 분석 대시보드")

# 3. 데이터 로드
data = load_data()

# 4. 페이지 제목 및 설명
st.title("🚗 국내 브랜드별 전기차 조회 페이지")
st.markdown("브랜드, 기종, 가격, 연비를 선택하여 원하는 전기차를 검색할 수 있습니다.")

# 5. 탭 생성
tab1, tab2, tab3 = st.tabs(["차량 검색", "데이터 분석", "브랜드별 분석"])

# 탭 1: 차량 검색
with tab1:
    # 필터 UI 구성
    st.write("### 필터 선택")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        brands = ["전체"] + sorted(data["브랜드"].unique())
        selected_brand = st.selectbox("브랜드", brands)
    
    with col2:
        if selected_brand != "전체":
            models = ["전체"] + sorted(data[data["브랜드"] == selected_brand]["기종"].unique())
        else:
            models = ["전체"] + sorted(data["기종"].unique())
        selected_model = st.selectbox("기종", models)
    
    with col3:
        prices = ["전체"] + sorted(data["가격(만원)"].unique())
        selected_price = st.selectbox("가격", prices)
    
    with col4:
        efficiency = ["전체"] + sorted(data["연비(km/kWh)"].unique())
        selected_efficiency = st.selectbox("연비", efficiency)
    
    # 데이터 필터링
    filtered_data = data.copy()
    
    if selected_brand != "전체":
        filtered_data = filtered_data[filtered_data["브랜드"] == selected_brand]
    
    if selected_model != "전체":
        filtered_data = filtered_data[filtered_data["기종"] == selected_model]
    
    if selected_price != "전체":
        filtered_data = filtered_data[filtered_data["가격(만원)"] == selected_price]
    
    if selected_efficiency != "전체":
        filtered_data = filtered_data[filtered_data["연비(km/kWh)"] == selected_efficiency]
    
    # 검색 결과 출력
    # st.write(f"### 검색 결과 ({len(filtered_data)}개)")
    # st.dataframe(filtered_data.drop(['평균가격', '평균연비'], axis=1), use_container_width=True)
    st.write(f"### 검색 결과 ({len(filtered_data)}개)")

    # URL을 클릭 가능한 링크로 변환
    def make_clickable(url):
        return f'<a href="{url}" target="_blank">링크</a>'

    # 출력할 데이터 준비
    display_data = filtered_data.drop(['평균가격', '평균연비'], axis=1).copy()
    display_data['보러가기'] = display_data['보러가기'].apply(make_clickable)

    # 데이터프레임 스타일링과 함께 출력
    st.write(
        display_data.to_html(escape=False, index=False),
        unsafe_allow_html=True
    )

    # CSS로 테이블 스타일 적용
    st.markdown("""
        <style>
            table {
                width: 100%;
            }
            th {
                text-align: left !important;
            }
            td {
                text-align: left !important;
            }
        </style>
        """, unsafe_allow_html=True)

# 탭 2: 데이터 분석
with tab2:
    st.write("### 가격 대비 연비 분석")
    
    # 넥쏘 제외 (연비 단위가 다름)
    analysis_data = data[data['기종'] != '2024 넥쏘']
    
    # 산점도 그래프
    fig_scatter = px.scatter(analysis_data, 
                            x='평균가격', 
                            y='평균연비',
                            color='브랜드',
                            size=[40] * len(analysis_data),
                            hover_data=['기종', '가격(만원)', '연비(km/kWh)'],
                            title='가격 대비 연비 분포')
    
    st.plotly_chart(fig_scatter, use_container_width=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        # 브랜드별 평균 가격
        fig_price = px.bar(analysis_data.groupby('브랜드')['평균가격'].mean().reset_index(),
                          x='브랜드',
                          y='평균가격',
                          title='브랜드별 평균 가격')
        st.plotly_chart(fig_price, use_container_width=True)
    
    with col2:
        # 브랜드별 평균 연비
        fig_efficiency = px.bar(analysis_data.groupby('브랜드')['평균연비'].mean().reset_index(),
                               x='브랜드',
                               y='평균연비',
                               title='브랜드별 평균 연비')
        st.plotly_chart(fig_efficiency, use_container_width=True)

# 탭 3: 브랜드별 분석
with tab3:
    selected_brand_analysis = st.selectbox("분석할 브랜드 선택", sorted(data["브랜드"].unique()))
    
    brand_data = data[data['브랜드'] == selected_brand_analysis]
    brand_data = brand_data[brand_data['기종'] != '2024 넥쏘']  # 넥쏘 제외
    
    col1, col2 = st.columns(2)
    
    with col1:
        # 선택된 브랜드의 차종별 가격 비교
        fig_brand_price = px.bar(brand_data,
                                x='기종',
                                y='평균가격',
                                title=f'{selected_brand_analysis} 차종별 가격')
        fig_brand_price.update_xaxes(tickangle=45)
        st.plotly_chart(fig_brand_price, use_container_width=True)
    
    with col2:
        # 선택된 브랜드의 차종별 연비 비교
        fig_brand_efficiency = px.bar(brand_data,
                                    x='기종',
                                    y='평균연비',
                                    title=f'{selected_brand_analysis} 차종별 연비')
        fig_brand_efficiency.update_xaxes(tickangle=45)
        st.plotly_chart(fig_brand_efficiency, use_container_width=True)
    
    # 연도별 출시 모델 수
    st.write(f"### {selected_brand_analysis} 연도별 출시 모델")
    year_count = brand_data['출시년도'].value_counts().sort_index()
    fig_year = px.bar(x=year_count.index, 
                      y=year_count.values,
                      title=f'{selected_brand_analysis} 연도별 출시 모델 수')
    st.plotly_chart(fig_year, use_container_width=True)

# 6. 푸터
st.markdown("---")
st.markdown("데이터 출처: 네이버 자동차")

# 메인으로 되돌아가기 버튼
if st.button("메인으로"):
    st.switch_page("project.py")
