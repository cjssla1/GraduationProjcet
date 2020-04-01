from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import datetime

driver = webdriver.PhantomJS('C:/Users/SAMSUNG/Downloads/phantomjs-2.1.1-windows/bin/phantomjs.exe')
#현재 첫 페이지만 크롤링함
driver.get("https://finance.naver.com/sise/sise_market_sum.nhn")

#페이지가 동적이라 스위치 눌러줘야함, 필요한 부분 선택하고
#불 필요한데 기본 선택되어있는 스위치 해제
driver.find_element_by_css_selector('#option7').click()
driver.find_element_by_css_selector('#option13').click()
driver.find_element_by_css_selector('#option19').click()
driver.find_element_by_css_selector('#option15').click()
driver.find_element_by_css_selector('#option21').click()
driver.find_element_by_css_selector('#option4').click()
driver.find_element_by_css_selector('#option6').click()
driver.find_element_by_css_selector('#option12').click()
#적용하기 버튼
driver.find_element_by_css_selector('#contentarea_left > div.box_type_m > form > div > div > div > a:nth-child(1)').click()

#주식 이름
names = driver.find_elements_by_css_selector('a.tltle')
#수치들 
numbers = driver.find_elements_by_css_selector('td.number')

#수치 줄로 엮기
lines = []
line = [numbers[0].text]
#날짜 추가용
today = datetime.datetime.today()
td = today.strftime('%Y-%m-%d')
x = 0 #이름 가져오기 위함

for i in range(1,len(numbers)):
    #줄 바꿈
    if i % 8 == 0:
        #종목 이름,날짜 추가
        line.append(names[x].text)
        x+=1
        line.append(td)
        lines.append(line)
        line = [numbers[i].text]
    elif i % 8 >= 1 and i % 8 <= 3:
        #불필요 제거
        continue
    else:
        line.append(numbers[i].text)


print(lines)

driver.quit()

