import streamlit as st
import mysql.connector
import pandas as pd

# sql 데이터베이스 연결 설정
connection = mysql.connector.connect(
    host="localhost",
    user="test",
    password="test",
    database="car_data"
)

# SQL 데이터 로드
def load_data():
    query = "SELECT car_name, brand_name, price FROM car_info"
    cursor = connection.cursor()
    cursor.execute(query)
    data = cursor.fetchall()  # 데이터 가져오기
    columns = [desc[0] for desc in cursor.description]  # 컬럼명 가져오기
    cursor.close()
    return pd.DataFrame(data, columns=columns)

# 데이터 로드
df = load_data()

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
    brands = ["전체"] + sorted(df["brand_name"].unique()) 
    selected_brand = st.selectbox("브랜드 선택:", brands)

# - 기종별: 브랜드>기종 
with col2:
    if selected_brand != "전체":
        models = ["전체"] + sorted(df[df["brand_name"] == selected_brand]["car_name"].unique())
    else:
        models = ["전체"] + sorted(df["car_name"].unique())
    selected_model = st.selectbox("차종 선택:", models)

# - 가격별: 가격 범주를 누르면 해당되는 가격들이 보여지기
with col3:
    price_categories = {
        "전체": lambda x: True,
        "2,000만원 미만": lambda x: x < 2000,
        "2,000~4,000만원": lambda x: 2000 <= x < 4000,
        "4,000~7,000만원": lambda x: 4000 <= x < 7000,
        "7,000만원 이상": lambda x: x >= 7000
    } # lambda 이용 - 미니함수처럼 조건을 한 줄로 간단히 표현하기 위해
    selected_price = st.selectbox("가격별 선택:", list(price_categories.keys())) # 키값만 반환, 딕셔너리키값을 리스트를 허용하는 selectbox에 넣기 위함

# 데이터 필터링
filtered_data = df.copy() # 필터링 작업에 새로운 변수를 원본 손실없이 사용하기 위해 copy

# 브랜드 필터링
if selected_brand != "전체":
    filtered_data = filtered_data[filtered_data["brand_name"] == selected_brand] # 사용자가 선택한 값과 일치 선상에 위치한 데이터 불러오기

# 기종 필터링
if selected_model != "전체":
    filtered_data = filtered_data[filtered_data["car_name"] == selected_model]

# 가격 필터링
price_filter = price_categories[selected_price] # 예를 들어 5~7%선택했다 -> price_filter = lambda x: 5 <= x < 7 범주에 맞는 데이터 찾는 조건
filtered_data = filtered_data[filtered_data["price"].apply(price_filter)] # 선택한 조건에 부합한 행만 남기기 위해


# 2. 검색 결과 출력
st.divider()
st.write(f"검색 결과: {len(filtered_data)}개")

# 3. 조회된 결과값
st.dataframe(filtered_data, use_container_width=True)

# 메인으로 되돌아가기 버튼
st.divider()
if st.button(f'메인으로'):
    st.switch_page("project.py")