import streamlit as st
import mysql.connector
from collections import Counter
import pandas as pd

st.title("인기있는 자동차!")

# sql 계정
connection = mysql.connector.connect(
    host="localhost",
    user="squirrel",
    password="squirrel",
    database="car_data_brand"
)

cursor = connection.cursor()
cursor.execute("SELECT AUTOMB_NM FROM test")

data = cursor.fetchall()

# def count_frequency(data):
#     counter = Counter(data)
    
#     sorted_items = counter.most_common(50)

    
#     cnt = 1
#     for item, count in sorted_items:
#         car_name = str(item).replace('"', '').replace('(', '').replace(')', '').replace(',', '').replace("'", '')
#         st.write(f"{cnt}위 {car_name} - {count}대")
#         cnt += 1
    
#     return sorted_items

# st.bar_chart(data.set_index('캐릭터')['선택횟수'])

def count_frequency(data):
    # Counter로 빈도수 계산
    counter = Counter(data)
    sorted_items = counter.most_common(50)  # 상위 50개만 가져오기
    
    # DataFrame 생성
    df = pd.DataFrame(sorted_items, columns=['차량명', '대수'])
    
    # 차량명 클리닝
    df['차량명'] = df['차량명'].apply(lambda x: str(x).replace('"', '').replace('(', '').replace(')', '').replace(',', '').replace("'", ''))
    
    # 순위 표시
    for idx, row in df.iterrows():
        st.write(f"{idx+1}위 {row['차량명']} - {row['대수']}대")
    
    # 막대 그래프 생성
    st.subheader("차량별 보유 대수 현황")
    
    # 그래프용 데이터 준비 (상위 20개만)
    chart_df = df.head(20)
    
    # 막대 그래프 표시
    st.bar_chart(data=chart_df.set_index('차량명')['대수'])
    
    return df

# 사용 예시
count_frequency(data)

if st.button(f'메인으로'):
    st.switch_page("project.py")