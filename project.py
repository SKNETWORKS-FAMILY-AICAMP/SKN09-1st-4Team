import streamlit as st

# 전기차 예외처리
def is_search():
    
    # 차 종류
    if '레이' in st.session_state.my_data:
        st.switch_page("pages/data_page.py")
    if '아이오닉' in st.session_state.my_data:
        st.switch_page("pages/data_page.py")
    if 'ZOE' in st.session_state.my_data:
        st.switch_page("pages/data_page.py")
    if '코나' in st.session_state.my_data:
        st.switch_page("pages/data_page.py")
    if '봉고' in st.session_state.my_data:
        st.switch_page("pages/data_page.py")
    if '니로' in st.session_state.my_data:
        st.switch_page("pages/data_page.py")
    if '쏘울' in st.session_state.my_data:
        st.switch_page("pages/data_page.py")
    if 'SM3' in st.session_state.my_data:
        st.switch_page("pages/data_page.py")
    if 'EV6' in st.session_state.my_data:
        st.switch_page("pages/data_page.py")
    if st.session_state.my_data == '레이':
        st.switch_page("pages/data_page.py")
    if st.session_state.my_data == '레이':
        st.switch_page("pages/data_page.py")
    if st.session_state.my_data == '레이':
        st.switch_page("pages/data_page.py")
    if st.session_state.my_data == '레이':
        st.switch_page("pages/data_page.py")
    if st.session_state.my_data == '레이':
        st.switch_page("pages/data_page.py")
    if st.session_state.my_data == '레이':
        st.switch_page("pages/data_page.py")
    if st.session_state.my_data == '레이':
        st.switch_page("pages/data_page.py")
    if st.session_state.my_data == '레이':
        st.switch_page("pages/data_page.py")
    if st.session_state.my_data == '레이':
        st.switch_page("pages/data_page.py")
    if st.session_state.my_data == '레이':
        st.switch_page("pages/data_page.py")
    if st.session_state.my_data == '레이':
        st.switch_page("pages/data_page.py")
    if st.session_state.my_data == '레이':
        st.switch_page("pages/data_page.py")

    # 지역 종류
    elif st.session_state.my_data == '서울':
        st.switch_page("pages/map_page.py")
    else:
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
    </style>
""", unsafe_allow_html=True)

st.markdown(
    """
    <style>
        .stApp {
            background-color: #444444;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Enter 키 입력시 실행할 동작

col1, col2 = st.columns([3, 1])
col3, col4 = st.columns([1, 2])
col5, col6, col7 = st.columns([1, 1, 1])
col8 = st.columns(1)

# header 밑으로 페이지를 보여준다.

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

     