import json
import re

# JSON 파일에서 데이터 읽기
with open("electric_cars_.json", "r", encoding="utf-8") as file:
    data = json.load(file)

# 데이터 변환 함수
def clean_price(json_data):
    for item in json_data:
        price_str = item["price"]
        # 숫자만 추출하고 문자열 합치기
        price_number = int(re.sub(r"[^\d]", "", price_str))
        item["price"] = price_number
    return json_data

# 변환된 데이터
converted_data = clean_price(data)

# 변환된 데이터를 파일에 저장하기
with open("electric_cars.json", "w", encoding="utf-8") as file:
    json.dump(converted_data, file, ensure_ascii=False, indent=4)
