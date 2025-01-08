import streamlit as st
import pandas as pd
import pymysql

st.title("인기있는 자동차!")

# sql 계정
connection = pymysql.connect(
    host="localhost",
    user="root",
    password="1234",
    database="car_data"
)

cursor = connection.cursor()
if cursor is None:
    print("cursor not connect!")

cursor.execute("SELECT * FROM car_info ORDER BY count DESC;")
rows = cursor.fetchall()

# 데이터프레임 생성 (열의 수를 맞춰서 수정)
data = pd.DataFrame(rows, columns=["ID", "차량명", "브랜드", '가격', '개수'])

# 첫 번째 열로 순위를 추가 (1~15)
data.insert(0, "순위", range(1, len(data) + 1))  # 1부터 순위 추가

# '가격' 열 삭제
data = data.drop("가격", axis=1, errors='ignore')  # '가격' 열이 없으면 무시

# 인기 순위 selectbox
nums = ['1위 ~ 5위', '5위 ~ 10위', '11위 ~ 15위']
best_nums = st.selectbox('인기 차량 순위', nums)

# 브랜드 selectbox
brands = ['기아', '현대', '제네시스']
best_brands = st.selectbox('브랜드별', ['모든 브랜드'] + brands)  # '모든 브랜드' 추가

# 스타일 적용 (왼쪽 정렬)
st.markdown(
    """
    <style>
    .stText, .stMarkdown {
        text-align: center;
    }
    table td, table th {
        text-align: left;
        padding: 8px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# 순위에 따라 데이터를 표시
if best_nums == nums[0]:
    filtered_data = data[:5]  # 1~5위
elif best_nums == nums[1]:
    filtered_data = data[5:10]  # 5~10위
elif best_nums == nums[2]:
    filtered_data = data[10:15]  # 11~15위
else:
    filtered_data = data  # 기본적으로 모든 데이터를 출력

# 브랜드에 따라 데이터를 표시
if best_brands != '모든 브랜드':
    filtered_data = filtered_data[filtered_data['브랜드'] == best_brands]  # 선택한 브랜드에 맞는 데이터 필터링

# 최종 필터링된 데이터 표시
st.dataframe(filtered_data, use_container_width=True, hide_index=True)

if st.button(f'메인으로'):
    st.switch_page("main_page.py")