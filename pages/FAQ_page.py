import streamlit as st

st.write(f"{st.session_state.my_data}에 대한 검색어입니다.")

if st.button(f'메인으로'):
    st.switch_page("project.py")