import streamlit as st
import mysql.connector
import pandas as pd


# 실행할 컴퓨터의 환경에 맞춰 설정 필요 ! ! ! !! ! !! !
db_config = {
    "host": "127.0.0.1",  # MySQL 서버 주소
    "port": 3306,
    "user": "root",       # MySQL 사용자 이름
    "password": "7276",   # MySQL 비밀번호
    "database": "car_data"  # 사용할 데이터베이스 이름
}

st.title("💵💰 전기차 가격 조회 💰💵")
st.write("전기차 새 차 가격 바로 알아보기")

values = st.slider("찾으실 차량의 가격범위를 설정해주세요(단위: 만원)", 0, 30000, (1000, 3000))
st.write("가격 설정:", values)
val1 = values[0]
val2 = values[1]


def fetch_data_from_mysql(val1, val2):
    try:
        # 데이터베이스 연결
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor(dictionary=True)  # 결과를 딕셔너리 형태로 반환

        # 테이블 존재 여부 확인
        cursor.execute("SHOW TABLES LIKE 'car_info'")
        if not cursor.fetchone():
            return None  # 테이블이 없으면 None 반환

        # 테이블에서 데이터 가져오기
        cursor.execute(f"SELECT * FROM car_info WHERE price BETWEEN {val1} AND {val2}")
        results = cursor.fetchall()  # 데이터 조회

        return results if results else None  # 데이터가 없으면 None 반환

    except mysql.connector.Error as err:
        st.error(f"MySQL Error: {err}")
        return None
    except Exception as e:
        st.error(f"An unexpected error occurred: {e}")
        return None
    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()






# MySQL 데이터 출력
st.write("### 저장된 전기차 가격표(단위: 만원)")
data = fetch_data_from_mysql(val1, val2)
if data:
    st.table(data)  # 테이블 형태로 데이터 출력
else:
    st.warning("아직 불러온 데이터가 없습니다.")


# 메인으로 되돌아가기 버튼
if st.button("메인으로"):
    st.switch_page("project.py")