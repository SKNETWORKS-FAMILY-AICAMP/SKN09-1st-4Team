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
url = "https://www.lotteautoauction.net/hp/pub/cmm/hom/faq/selectFaqList.do"
driver.get(url)
time.sleep(1)  # 페이지 로드 대기

# 3. 데이터 크롤링
faq_data = []
faq_id_idx = []

cars_area_elems = driver.find_elements(By.CSS_SELECTOR, ".tblFaq tbody")

for cars_area_elem in cars_area_elems:
    cars_question_elems = cars_area_elem.find_elements(By.CSS_SELECTOR, "tr td dl dt")
    cars_value_elems = cars_area_elem.find_elements(By.CSS_SELECTOR, "tr td dl dd")
    
    num = driver.find_elements(By.CLASS_NAME, 'dl_faq')
    for i in range(10):
        faq_id_idx.append(num[i].get_attribute("id"))
    

    for i, (cars_question, cars_value) in enumerate(zip(cars_question_elems, cars_value_elems)):

        car_btn = driver.find_element(By.XPATH, f'//*[@id="{faq_id_idx[i]}"]')
        car_btn.click()
        time.sleep(1)

        # 차종명
        a_tag_question = cars_question.find_element(By.CSS_SELECTOR, ".faq_tit")
        question = a_tag_question.text.strip()
        # 브랜드명
        
        value = driver.find_element(By.ID, f"contents_{i+1}").get_attribute("innerHTML")

        # 데이터 저장
        faq_data.append({
            "question": question,
            "value": value,
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
df = pd.DataFrame(faq_data)

# 6. JSON으로 저장
with open("FAQ_cars.json", "w", encoding="utf-8") as json_file:
    json.dump(faq_data, json_file, ensure_ascii=False, indent=4)

print("데이터 저장 완료: JSON 파일")

