import streamlit as st
import mysql.connector
import json
import subprocess
import pandas as pd
import time

db_config = {
    "host": "127.0.0.1",  # MySQL 서버 주소
    "port": 3306,
    "user": "root",       # MySQL 사용자 이름
    "password": "7276",   # MySQL 비밀번호
    "database": "projectdb"  # 사용할 데이터베이스 이름
}

def json_sql():
    # MySQL 연결 설정
    

    # JSON 파일 경로
    json_file_path = "../SKN09-1st-4Team-main/electric_cars_price.json"

    # 데이터베이스 연결
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()
        # JSON 파일 읽기
        with open(json_file_path, "r", encoding="utf-8") as file:
            car_data = json.load(file)

        # 테이블 초기화
        cursor.execute("DROP TABLE IF EXISTS car_prices")
        st.info("기존 테이블 삭제 완료.")

        # 테이블 생성
        create_table_query = """
        CREATE TABLE IF NOT EXISTS car_prices (
            id INT AUTO_INCREMENT PRIMARY KEY,
            title VARCHAR(50),
            brand_name VARCHAR(100),
            price INT
        );
        """
        cursor.execute(create_table_query)

        # 데이터 삽입
        insert_query = """
            INSERT INTO car_prices (title, brand_name, price)
            VALUES (%s, %s, %s)
        """
        for car in car_data:
            values = (
                car.get("title", "Unknown"),  # JSON 키를 읽고, 없을 경우 기본값 설정
                car.get("brand_name", "Unknown"),
                int(car.get("price", 0))  # 숫자로 변환
            )
            cursor.execute(insert_query, values)

        # 커밋 및 연결 종료
        connection.commit()
        st.success(f"{cursor.rowcount} rows inserted into the database.")

    except mysql.connector.Error as err:
        st.error(f"MySQL Error: {err}")
    except json.JSONDecodeError:
        st.error("Error reading the JSON file. Please check the file format.")
    except Exception as e:
        st.error(f"An unexpected error occurred: {e}")
    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()


def fetch_data_from_mysql():
    try:
        # 데이터베이스 연결
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor(dictionary=True)  # 결과를 딕셔너리 형태로 반환

        # 테이블 존재 여부 확인
        cursor.execute("SHOW TABLES LIKE 'car_prices'")
        if not cursor.fetchone():
            return None  # 테이블이 없으면 None 반환

        # 테이블에서 데이터 가져오기
        cursor.execute("SELECT * FROM car_prices")
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



st.title("💵💰 전기차 가격 조회 💰💵")
st.write("전기차 새 차 가격 바로 알아보기")

# 가격 최신화 버튼
if st.button("가격 최신화"):
    result = subprocess.run(
        ["python", "../price_update.py"], capture_output=True, text=True
    )
    time.sleep(20)
    st.text(result.stdout)  # 스크립트 실행 결과 출력
    json_sql()  # JSON 파일을 데이터베이스에 삽입



# MySQL 데이터 출력
st.write("### 저장된 전기차 가격표(단위: 만원)")
data = fetch_data_from_mysql()
if data:
    st.table(data)  # 테이블 형태로 데이터 출력
else:
    st.warning("아직 불러온 데이터가 없습니다. 최신화 버튼을 눌러주세요.")



# 메인으로 버튼
if st.button("메인으로"):
    st.write("메인 페이지로 이동!")
    st.experimental_rerun()
