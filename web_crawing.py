import urllib.parse
import urllib.request
import mysql.connector
import xml.etree.ElementTree as ET
import math
import json
from collections import Counter

# API 키와 기본 URL 설정
API_KEY = '6f43a308aea74ad6855c719641eb85eb'
BASE_URL = 'https://openapi.gg.go.kr/OFCUSEELCTYCAR'


# URL 파라미터 설정
count = 2
params = {
    'KEY': API_KEY,
    'Type' : "xml",
    'pIndex': 1,
    'pSize': 1
#    'SIGUN_CD': '41310'  # 구리시
}

# URL 생성
url = f"{BASE_URL}?{urllib.parse.urlencode(params)}"

# API 요청
response = urllib.request.urlopen(url)

# 응답 읽기
response_body = response.read().decode('utf-8')
root = ET.fromstring(response_body)

# 전체 데이터 수 가져오기
total_count = int(root.find('.//head/list_total_count').text)
pages_needed = math.ceil(total_count / 100)

# 차량 데이터를 저장할 리스트
car_names = []

# db 연결 객체 생성
for page in range(1, pages_needed + 1):
   params = {
       'KEY': API_KEY,
       'Type': "xml",
       'pIndex': page,
       'pSize': 100
   }
   
   url = f"{BASE_URL}?{urllib.parse.urlencode(params)}"
   response = urllib.request.urlopen(url)
   response_body = response.read().decode('utf-8')
   root = ET.fromstring(response_body)
   
   rows = root.findall('.//row')
   
   for row in rows:
       automb_nm = row.find('AUTOMB_NM').text if row.find('AUTOMB_NM') is not None else None
       if automb_nm:
            normalized_name = ''.join(automb_nm.split())  # 모든 공백 제거
            car_names.append(normalized_name)
# Counter로 빈도수 계산
car_counts = Counter(car_names)

# sql 

# sql 데이터 넣기
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="car_data"
)

cursor = connection.cursor()

with open('SKN09-1st-4Team-main/electric_cars_.json', 'r', encoding='utf-8') as f:
    car_prices = json.load(f)


# 기존 테이블 삭제 (있다면)
cursor.execute("DROP TABLE IF EXISTS car_info")


# 새로운 테이블 생성
create_table_sql = """
CREATE TABLE car_info (
   car_id INT AUTO_INCREMENT PRIMARY KEY,
   car_name VARCHAR(255),
   brand_name VARCHAR(255),
   price VARCHAR(255),
   count INT
)
"""

cursor.execute(create_table_sql)

car_json_mix = []
for car in car_prices:

    count = car_counts.get(car['title'], 0)

    car_json_mix.append((
        car['title'],
        car['brand_name'],
        car['price'],
        count
    ))


# 데이터 삽입
sql = "INSERT INTO car_info (car_name, brand_name, price, count) VALUES (%s, %s, %s, %s)"
cursor.executemany(sql, car_json_mix)

connection.commit()
cursor.close()
connection.close()