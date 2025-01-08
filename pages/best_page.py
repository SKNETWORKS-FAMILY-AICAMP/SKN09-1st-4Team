# import streamlit as st
# import pandas as pd
# import pymysql

# st.title("인기있는 자동차!")

# # sql 계정
# connection = pymysql.connect(
#     host="localhost",
#     user="root",
#     password="1234",
#     database="car_data"
# )

# cursor = connection.cursor()
# if cursor is None:
#     print("cursor not connect!")

# cursor.execute("SELECT * FROM car_info ORDER BY count DESC;")
# rows = cursor.fetchall()

# # 데이터프레임 생성 (열의 수를 맞춰서 수정)
# data = pd.DataFrame(rows, columns=["ID", "차량명", "브랜드", '가격', '개수'])

# # 첫 번째 열로 순위를 추가 (1~15)
# data.insert(0, "순위", range(1, len(data) + 1))  # 1부터 순위 추가

# # '가격' 열 삭제
# data = data.drop("가격", axis=1, errors='ignore')  # '가격' 열이 없으면 무시

# # selectbox
# nums = ['1위 ~ 5위', '5위 ~ 10위', '11위 ~ 15위']
# best_nums = st.selectbox('인기 차량 순위', nums)

# brands = ['기아', '현대', '제네시스']
# best_brands = st.selectbox('브랜드별', ['모든 브랜드'] + brands)  # '모든 브랜드' 추가

# # 스타일 적용 (왼쪽 정렬)
# st.markdown(
#     """
#     <style>
#     .stText, .stMarkdown {
#         text-align: center;
#     }
#     table td, table th {
#         text-align: left;
#         padding: 8px;
#     }
#     </style>
#     """,
#     unsafe_allow_html=True,
# )

# # 차량명 클릭 후 이미지를 표시하기 위한 코드
# def display_image(car_name):
#     # 예시로 로컬 경로에 있는 이미지를 표시한다고 가정
#     image_path = f'.C:\Users\USER\Desktop\test_img\{car_name}.jpg'  # 차량명에 맞는 이미지 파일 경로 (실제 경로로 수정 필요)
    
#     try:
#         st.image(image_path, caption=car_name, use_column_width=True)
#     except Exception as e:
#         st.error(f"이미지를 찾을 수 없습니다: {e}")

# # 순위에 따라 데이터를 표시
# if best_nums == nums[0]:
#     filtered_data = data[:5]  # 1~5위
# elif best_nums == nums[1]:
#     filtered_data = data[5:10]  # 5~10위
# elif best_nums == nums[2]:
#     filtered_data = data[10:15]  # 11~15위
# else:
#     filtered_data = data  # 기본적으로 모든 데이터를 출력

# # 브랜드에 따라 데이터를 표시
# if best_brands != '모든 브랜드':
#     filtered_data = filtered_data[filtered_data['브랜드'] == best_brands]  # 선택한 브랜드에 맞는 데이터 필터링

# # 최종 필터링된 데이터 표시
# selected_car_name = st.selectbox('차량을 선택하세요', filtered_data['차량명'])

# # 차량을 선택한 후 해당 이미지 출력
# display_image(selected_car_name)

# st.dataframe(filtered_data, use_container_width=True, hide_index=True)











# import streamlit as st
# import pandas as pd
# import pymysql

# st.title("인기있는 자동차!")

# # sql 계정
# connection = pymysql.connect(
#     host="localhost",
#     user="root",
#     password="1234",
#     database="car_data"
# )

# cursor = connection.cursor()
# if cursor is None:
#     print("cursor not connect!")

# cursor.execute("SELECT * FROM car_info ORDER BY count DESC;")
# rows = cursor.fetchall()

# # 데이터프레임 생성 (열의 수를 맞춰서 수정)
# data = pd.DataFrame(rows, columns=["ID", "차량명", "브랜드", '가격', '개수'])

# # 첫 번째 열로 순위를 추가 (1~15)
# data.insert(0, "순위", range(1, len(data) + 1))  # 1부터 순위 추가

# # '가격' 열 삭제
# data = data.drop("가격", axis=1, errors='ignore')  # '가격' 열이 없으면 무시

# # selectbox
# nums = ['1위 ~ 5위', '5위 ~ 10위', '11위 ~ 15위']
# best_nums = st.selectbox('인기 차량 순위', nums)

# brands = ['기아', '현대', '제네시스']
# best_brands = st.selectbox('브랜드별', ['모든 브랜드'] + brands)  # '모든 브랜드' 추가

# # 스타일 적용 (왼쪽 정렬)
# st.markdown(
#     """
#     <style>
#     .stText, .stMarkdown {
#         text-align: center;
#     }
#     table td, table th {
#         text-align: left;
#         padding: 8px;
#     }
#     </style>
#     """,
#     unsafe_allow_html=True,
# )

# # 차량명 클릭 후 이미지를 표시하기 위한 코드
# def display_image(car_name):
#     # 예시로 로컬 경로에 있는 이미지를 표시한다고 가정
#     image_path = f'./images/{car_name}.jpg'  # 차량명에 맞는 이미지 파일 경로 (실제 경로로 수정 필요)
    
#     try:
#         st.image(image_path, caption=car_name, use_column_width=True)
#     except Exception as e:
#         st.error(f"이미지를 찾을 수 없습니다: {e}")

# # 순위에 따라 데이터를 표시
# if best_nums == nums[0]:
#     filtered_data = data[:5]  # 1~5위
# elif best_nums == nums[1]:
#     filtered_data = data[5:10]  # 5~10위
# elif best_nums == nums[2]:
#     filtered_data = data[10:15]  # 11~15위
# else:
#     filtered_data = data  # 기본적으로 모든 데이터를 출력

# # 브랜드에 따라 데이터를 표시
# if best_brands != '모든 브랜드':
#     filtered_data = filtered_data[filtered_data['브랜드'] == best_brands]  # 선택한 브랜드에 맞는 데이터 필터링

# # 최종 필터링된 데이터 표시
# selected_car_name = st.selectbox('차량을 선택하세요', filtered_data['차량명'])

# # 차량을 선택한 후 해당 이미지 출력
# display_image(selected_car_name)

# st.dataframe(filtered_data, use_container_width=True, hide_index=True)


#-------------------------------------------------------------------------------------------------------------------------

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



#-------------------------------------------------------------------------------------------------------------

# 가격만있는거


# import streamlit as st
# import pandas as pd
# import pymysql

# st.title("인기있는 자동차!")

# # sql 계정
# connection = pymysql.connect(
#     host="localhost",
#     user="root",
#     password="1234",
#     database="car_data"
# )

# cursor = connection.cursor()
# if cursor is None:
#     print("cursor not connect!")

# cursor.execute("SELECT * FROM car_info ORDER BY count DESC;")
# rows = cursor.fetchall()

# # 데이터프레임 생성 (열의 수를 맞춰서 수정)
# data = pd.DataFrame(rows, columns=["ID", "차량명", "브랜드", '가격', '개수'])

# # 첫 번째 열로 순위를 추가 (1~15)
# data.insert(0, "순위", range(1, len(data) + 1))  # 1부터 순위 추가

# # '가격' 열 삭제
# data = data.drop("가격", axis=1, errors='ignore')  # '가격' 열이 없으면 무시

# # 선택된 순위에 따라 데이터 표시
# nums = ['1위 ~ 5위', '5위 ~ 10위', '11위 ~ 15위']
# best_nums = st.selectbox('인기 차량 순위', nums)

# # 스타일 적용 (왼쪽 정렬)
# st.markdown(
#     """
#     <style>
#     .stText, .stMarkdown {
#         text-align: center;
#     }
#     table td, table th {
#         text-align: left;
#         padding: 8px;
#     }
#     </style>
#     """,
#     unsafe_allow_html=True,
# )

# # 순위에 따라 데이터를 표시, 인덱스 숨기기
# if best_nums == nums[0]:
#     st.dataframe(data[:5], use_container_width=True, hide_index=True)  # 1~5위
# elif best_nums == nums[1]:
#     st.dataframe(data[5:10], use_container_width=True, hide_index=True)  # 5~10위
# elif best_nums == nums[2]:
#     st.dataframe(data[10:15], use_container_width=True, hide_index=True)  # 11~15위


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


if st.button(f'메인으로'):
    st.switch_page("project.py")