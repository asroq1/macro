# -*- coding: utf-8 -*-
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


member_num = "1234567890" # 회원번호
pwd = "1111111111" # 비밀번호
depart_station = "동탄" # 출발역 
arrival_station = "수서" # 도착역
depart_date = "20210926" # 출발 날짜 YYYYMMDD 형식
depart_time = "14" # 출발 시간 00, 02, 04, ... ,20, 22 형식 
number_of_trains = 4 # 검색 결과 상단에서부터 예약 가능 여부 확인할 기차 수 


# 입력한 기차역은 아래 리스트에 있어야 함.
station_list = ["수서", "동탄", "평택지제", "천안아산", "오송", "대전", "김천(구미)", "동대구",
                "신경주", "울산(통도사)", "부산", "공주", "익산", "정읍", "광주송정", "나주", "목포"]


driver = webdriver.Chrome("chromedriver")
driver.get('https://etk.srail.co.kr/cmc/01/selectLoginForm.do')
driver.implicitly_wait(15)

# 로그인
driver.find_element(By.ID, 'srchDvNm01').send_keys(member_num) # 회원번호
driver.find_element(By.ID, 'hmpgPwdCphd01').send_keys(pwd) # 비밀번호
driver.find_element(By.XPATH, '//*[@id="login-form"]/fieldset/div[1]/div[1]/div[2]/div/div[2]/input').click()
driver.implicitly_wait(5)

# 기차 조회 페이지로 이동
driver.get('https://etk.srail.kr/hpg/hra/01/selectScheduleList.do')
driver.implicitly_wait(5)

# 출발지 입력
dep_stn = driver.find_element(By.ID, 'dptRsStnCdNm')
dep_stn.clear()
dep_stn.send_keys(depart_station)

# 도착지 입력
arr_stn = driver.find_element(By.ID, 'arvRsStnCdNm')
arr_stn.clear()
arr_stn.send_keys(arrival_station)

# 출발 날짜
elm_dptDt = driver.find_element(By.ID, "dptDt")
driver.execute_script("arguments[0].setAttribute('style','display: True;')", elm_dptDt)
Select(driver.find_element(By.ID,"dptDt")).select_by_value(depart_date)

# 출발 시간
elm_dptTm = driver.find_element(By.ID, "dptTm")
driver.execute_script("arguments[0].setAttribute('style','display: True;')", elm_dptTm)
Select(driver.find_element(By.ID, "dptTm")).select_by_visible_text(depart_time)

# 조회하기 버튼 클릭
driver.find_element(By.XPATH, "//input[@value='조회하기']").click()
driver.implicitly_wait(5)

reserved = False

while True:
    for i in range(1, number_of_trains+1):
        standard_seat = driver.find_element(By.CSS_SELECTOR, f"#result-form > fieldset > div.tbl_wrap.th_thead > table > tbody > tr:nth-child({i}) > td:nth-child(7)").text

        if "예약하기" in standard_seat:
            print("예약 가능")          
            driver.find_element(By.XPATH, f"/html/body/div[1]/div[4]/div/div[3]/div[1]/form/fieldset/div[6]/table/tbody/tr[{i}]/td[7]/a/span").click()
            reserved = True
            break

    if not reserved:
        # 5초 기다리기
        time.sleep(5)     
        # 다시 조회하기
        submit = driver.find_element(By.XPATH, "//input[@value='조회하기']")
        driver.execute_script("arguments[0].click();", submit)
        print("새로고침")
        driver.implicitly_wait(10)
        time.sleep(1)
    else:
        break