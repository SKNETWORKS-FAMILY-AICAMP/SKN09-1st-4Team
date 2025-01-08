import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import pandas as pd
import time

# 1. Selenium WebDriver 설정
chrome_options = Options()
chrome_options.add_argument("--headless")  # 브라우저 창 없이 실행
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

service = Service('chromedriver.exe')  # Chromedriver 경로 설정
driver = webdriver.Chrome(service=service, options=chrome_options)

# 2. 웹사이트 열기
url = "https://auto.danawa.com/newcar/?listSortType=1&tab=all&rangeMinPrice=&rangeMaxPrice=&searchKeyword=&listCount=30&page=1&brandList=303,307,304&segmentList=&attributeList=2|20|S,2|964|S"
driver.get(url)
time.sleep(3)  # 페이지 로드 대기

# 3. 데이터 크롤링
car_data = []

cars_area_elems = driver.find_elements(By.CSS_SELECTOR, ".modelList")

for cars_area_elem in cars_area_elems:
    cars_info_elems = cars_area_elem.find_elements(By.CSS_SELECTOR, "li .info")
    cars_price_elems = cars_area_elem.find_elements(By.CSS_SELECTOR, "li .right")

    for model_name_elem, brand_name_elem, price_elem in zip(cars_info_elems, cars_info_elems, cars_price_elems):
        # 차종명
        a_tag_model = model_name_elem.find_element(By.CSS_SELECTOR, ".detail .detail_middle a.sendGA")
        title = a_tag_model.text.strip()

        # 브랜드명
        a_tag_brand = brand_name_elem.find_element(By.CSS_SELECTOR, ".detail .detail_middle .name img")
        brand = a_tag_brand.get_attribute("alt").strip()

        # 가격
        a_tag_price = price_elem.find_element(By.CSS_SELECTOR, ".row .price .box__selling")
        price = a_tag_price.text.strip()

        # 데이터 저장
        car_data.append({
            "title": title,
            "brand_name": brand,
            "price": price
        })
    

    # 다음 페이지 버튼 클릭 (더 이상 버튼이 없으면 종료)
    try:
        next_button = driver.find_element(By.CSS_SELECTOR, '.next')
        if "disable" in next_button.get_attribute("class"):
            break
        next_button.click()
        time.sleep(2)  # 다음 페이지 로드 대기
    except:
        break

# 4. Selenium 종료
driver.quit()

# 5. DataFrame으로 저장
df = pd.DataFrame(car_data)

# 6. JSON으로 저장
with open("electric_cars.json", "w", encoding="utf-8") as json_file:
    json.dump(car_data, json_file, ensure_ascii=False, indent=4)

print("데이터 저장 완료: JSON 파일")

