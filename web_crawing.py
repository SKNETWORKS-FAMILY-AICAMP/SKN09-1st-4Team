import urllib.parse
import urllib.request
import mysql.connector
import xml.etree.ElementTree as ET
import math
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
           car_names.append(automb_nm)

# Counter로 빈도수 계산
car_counts = Counter(car_names)
top_50_cars = car_counts.most_common(50)

# sql 

# sql 데이터 넣기
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="price"
)

cursor = connection.cursor()

# 데이터 삽입
sql = "INSERT INTO car_n (AUTOMB_NM, cnt) VALUES (%s, %s)"
cursor.executemany(sql, top_50_cars)

connection.commit()
cursor.close()
connection.close()