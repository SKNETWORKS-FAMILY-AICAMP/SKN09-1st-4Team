import streamlit as st

st.write("price_page입니다.")

if st.button(f'메인으로'):
    st.switch_page("project.py")