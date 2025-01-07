import streamlit as st
import mysql.connector
import pandas as pd
# import numpy as np

# # SQL 데이터베이스 연결 함수
# def create_connection():
#     connection = mysql.connector.connect(
#         host="localhost",
#         user="",
#         password="",
#         database=""
#     )
#     return connection

# 데이터 로드
data = {
    "Product": ["A", "B", "C", "D"],
    "Sales": [500, 300, 400, 600],
    "Growth (%)": [10, -5, 15, 7]
}
# st.json(data, expanded=True) # json 파일을 불러올 때 사용
df = pd.DataFrame(data)

# FAQ 데이터 예시
faq_data = {
    "Product": ["A", "B", "C", "D"],
    "Review": [
        "A 제품은 안정적인 성능과 저렴한 가격으로 추천받고 있습니다.",
        "B 제품은 신뢰성은 좋지만 성장률이 낮습니다.",
        "C 제품은 높은 성장률과 인기를 보이고 있습니다.",
        "D 제품은 성장률은 평균적이지만 판매량이 좋습니다."
    ]
}
faq_df = pd.DataFrame(faq_data)

# Streamlit 페이지 설정
st.set_page_config(layout="wide", page_title="국내 브랜드별 전기차 조회")


# 페이지 제목 및 설명
st.header("🚗 국내 브랜드별 전기차 조회 페이지")
st.write("원하시는 전기차의 브랜드·기종·가격별로 선택해주세요.")
st.divider()

# 1. 필터링
# - 브랜드별, 기종별, 가격별(가격 범주로 잡기)
# - 셀렉박스/ 한 줄 배열
st.write("### 필터 선택")

col1, col2, col3 = st.columns(3)

# - 브랜드별
with col1:
    brands = ["전체"] + sorted(df["Product"].unique()) # 데이터베이스에서 브랜드명에 해당하는 부분 "Product"에 넣기
    selected_brand = st.selectbox("브랜드 선택:", brands)

# - 기종별: 브랜드>기종 
with col2:
    if selected_brand != "전체":
        models = ["전체"] + sorted(df[df["Product"] == selected_brand]["Sales"].unique())
    else:
        models = ["전체"] + sorted(df["Sales"].unique()) # 여기는 차종 넣기
    selected_model = st.selectbox("차종 선택:", models)

# - 가격별: 가격 범주를 누르면 해당되는 가격들이 보여지기
with col3:
    price_categories = {
        "전체": lambda x: True,
        "0% 미만": lambda x: x < 0,
        "0~10%": lambda x: 0 <= x < 10,
        "10% 이상": lambda x: x >= 10
    } # lambda 이용 - 미니함수처럼 조건을 한 줄로 간단히 표현하기 위해
    selected_price = st.selectbox("가격별 선택:", list(price_categories.keys())) # 키값만 반환, 딕셔너리키값을 리스트를 허용하는 selectbox에 넣기 위함

# 데이터 필터링
filtered_data = df.copy() # 필터링 작업에 새로운 변수를 원본 손실없이 사용하기 위해 copy

# 브랜드 필터링
if selected_brand != "전체":
    filtered_data = filtered_data[filtered_data["Product"] == selected_brand] # 사용자가 선택한 값과 일치 선상에 위치한 데이터 불러오기

# 기종 필터링
if selected_model != "전체":
    filtered_data = filtered_data[filtered_data["Sales"] == selected_model]

# 가격 필터링
price_filter = price_categories[selected_price] # 예를 들어 5~7%선택했다 -> price_filter = lambda x: 5 <= x < 7 범주에 맞는 데이터 찾는 조건
filtered_data = filtered_data[filtered_data["Growth (%)"].apply(price_filter)] # 선택한 조건에 부합한 행만 남기기 위해


# 2. 검색 결과 출력
st.divider()
st.write(f"검색 결과: {len(filtered_data)}개")

# 3. 조회된 결과값
st.dataframe(filtered_data, use_container_width=True)

# - 텍스트 좌측 정렬
st.markdown(
    """
    <style>
    .stText, .stMarkdown {
        text-align: left;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# 4. 결과값에 적용되는 Review 보여주기 (faq 후기 데이터 적용)
st.divider()
if not filtered_data.empty:
    st.write("### 실사용자 후기")
    for brand in filtered_data["Product"].unique():  # 고유 제품명을 순회
        # 리뷰 데이터에서 해당 제품에 해당하는 리뷰를 가져오기
        review_row = faq_df[faq_df["Product"] == brand]
        if not review_row.empty:  # 해당 리뷰가 존재하면
            review = review_row["Review"].values[0]  # 리뷰 값을 가져옴
            st.write(f"**{brand}:** {review}")
        else:
            st.write(f"**{brand}:** 관련 리뷰가 없습니다.")
else:
    st.write("관련 리뷰가 없습니다.")

# 메인으로 되돌아가기 버튼
if st.button(f'메인으로'):
    st.switch_page("project.py")