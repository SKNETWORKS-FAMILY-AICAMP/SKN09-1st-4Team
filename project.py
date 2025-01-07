import streamlit as st
import json
from PIL import Image


with open('electric_cars_.json', 'r', encoding='utf-8') as f:
    car_info = json.load(f)

# 전기차 예외처리
def is_search():
    for car in car_info:
       if car['title'].lower() in st.session_state.my_data.lower():
           st.switch_page("pages/best_page.py")
       elif car['brand_name'].lower() in st.session_state.my_data.lower():
           st.switch_page("pages/brand_page.py")
    numbers = ''.join(c for c in st.session_state.my_data if c.isdigit())
    if numbers:  
        st.switch_page("pages/price_page.py")
    with col3:
        st.write("다시 입력해주세요")  


# 생성 페이지 내용
st.markdown("<h1 style='text-align: center;'>전기차톡</h1>", unsafe_allow_html=True)

st.markdown("""
    <style>
    /* 버튼의 위치 조정 */
    div.row-widget.stButton {
        padding-top: 22px;  # 이 값을 조절하여 버튼 위치 미세 조정
    }
    
    /* input box와 버튼의 높이 통일 */
    .stTextInput input {
        height: 42px;
    }
    
    .stButton button {
        height: 42px;
    }
            
    .centered-image {
        display: flex;
        justify-content: center;
        margin-bottom: 2rem;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown(
    """
    <style>
        .stApp {
            background-color: #000000;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Enter 키 입력시 실행할 동작

car_img = Image.open('electronic_car.jpg')
col_img1, col_img2, col_img3 = st.columns([2, 1, 2])
with col_img2:
    st.image(car_img, use_container_width=True)

col1, col2 = st.columns([3, 1])
col3, col4 = st.columns([1, 1])
col5, col6, col7 = st.columns([1, 1, 1])
col8 = st.columns(1)

# header 밑으로 페이지를 보여준다.
car_img = Image.open('electronic_car.jpg')

with col1:
    st.session_state.my_data = st.text_input("", placeholder="원하는 전기차를 입력해주세요.")

with col2:
    container = st.container()
    st.write("")  
    if st.button(f'검색'):  
         is_search()

with col5:
    if st.button(f'가격별', use_container_width=True):
            st.switch_page("pages/price_page.py")
with col6:
    if st.button(f'인기차종', use_container_width=True):
            st.switch_page("pages/best_page.py")
with col7:
    if st.button(f'브랜드별', use_container_width=True):
            st.switch_page("pages/brand_page.py")
    
with col8[0]:
    if st.button(f'FAQ', use_container_width=True):
            st.switch_page("pages/FAQ_page.py")