import streamlit as st
from collections import Counter
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


data = pd.DataFrame(rows, columns = ["ID", "차량명", "브랜드",'가격', '개수'])
#data = data.drop(data.columns[0], axis=1) 첫 번째 행 지운다면서 '순위' 지움 .띠바~.
#data.reset_index(drop=True, inplace=True)   # 기존 인덱스 삭제


nums = ['1위 ~ 5위', '5위 ~ 10위', '11위 ~ 15위']
best_nums = st.selectbox('인기 차량 순위', nums)



# def display_data(selected_data):  # html로 기존 인덱스 삭제   되긴 하는데 표가 작아져서 맘에 안듬
#     st.markdown(selected_data.to_html(index=False), unsafe_allow_html=True)   


if best_nums == nums[0]:
    st.table(data[:5])
elif best_nums == nums[1]:
    st.table(data[5:10])
elif best_nums == nums[2]:
    st.table(data[10:15])



#-------------------------------------------------------------------------------------------------------------

# st.title("인기있는 자동차!")

# # sql 계정
# connection = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="1234",
# #    database="car_data_brand"
# )

# cursor = connection.cursor()
# cursor.execute("SELECT AUTOMB_NM FROM test")

# data = cursor.fetchall()

# def count_frequency(data):
#     # Counter로 빈도수 계산
#     counter = Counter(data)
#     sorted_items = counter.most_common(50)  # 상위 50개만 가져오기
    
#     # DataFrame 생성
#     df = pd.DataFrame(sorted_items, columns=['차량명', '대수'])
    
#     # 차량명 클리닝 - 옆에꺼 없애는 용도
#     df['차량명'] = df['차량명'].apply(lambda x: str(x).replace('"', '').replace('(', '').replace(')', '').replace(',', '').replace("'", ''))
    
#     # 순위 표시
#     for idx, row in df.iterrows():
#         st.write(f"{idx+1}위 {row['차량명']} - {row['대수']}대")
    
#     # 막대 그래프 생성
#     st.subheader("차량별 보유 대수 현황")
    
#     # 그래프용 데이터 준비 (상위 20개만)
#     chart_df = df.head(20)
    
#     # 막대 그래프 표시
#     st.bar_chart(data=chart_df.set_index('차량명')['대수'])
    
#     return df

# # 함수 생성
# count_frequency(data)

# if st.button(f'메인으로'):
#     st.switch_page("project.py")