import time
from selenium import webdriver

browser = webdriver.Chrome('/Users/jobflexqa2.MIDASIT/PycharmProjects/chromedriver_win32/chromedriver')
browser.implicitly_wait(3)
browser.get('https://st-ogu59-admin-recruiter-co-kr.midasweb.net/cus/login')

browser.find_element_by_name('id').send_keys('qaqc09')  # 아이디 입력
browser.find_element_by_name('password').send_keys('test1357@#')  # 비밀번호 입력

browser.find_element_by_xpath('/html/body/form/div[1]/div[3]/div[1]/button').click()   # 로그인 버튼 클릭

browser.find_element_by_xpath('/html/body/form/article/div/div[2]/button').click()    # 팝업창 닫기 클릭

browser.find_element_by_xpath('/html/body/div/div[2]/div/section/a[2]/div/div/div[2]').click()    # [2.0] 클릭

browser.find_element_by_xpath('/html/body/div[2]/button').click()  # 좌측 UI 열기

browser.find_element_by_xpath('/html/body/div[2]/nav/ul/li[1]/a').click()  # 채용공고관리 클릭

browser.find_element_by_xpath('/html/body/div[2]/nav/ul/li[1]/ul/li[2]/a').click()  # 채용공고등록 클릭

browser.find_element_by_xpath('/html/body/div[2]/div/div/form/table/tbody/tr[1]/td/input').click()  # 공고명 텍스트박스 클릭

browser.find_element_by_name('recruitNoticeName').send_keys('selenium_auto_title1')  # 공고명 입력하기

browser.find_element_by_xpath('/html/body/div[2]/div/div/form/table/tbody/tr[2]/td/label/input').click()  # 기본이미지 체크박스 체크

browser.find_element_by_xpath('/html/body/div[2]/div/div/form/table/tbody/tr[3]/td/span[1]/label/input').click()   # 일반채용 라디오버튼 클릭

browser.find_element_by_xpath('/html/body/div[2]/div/div/form/table/tbody/tr[4]/td/label/select').click()  # 코드선택 셀렉박스 클릭

time.sleep(2)

from selenium.webdriver.support.select import Select
select = Select(browser.find_element_by_id('frm-recruitClassCodeSn'))
select.select_by_index(1)

browser.find_element_by_xpath('/html/body/div[2]/div/div/form/table/tbody/tr[5]/td/div[2]/div[1]/label/select').click()

time.sleep(2)

from selenium.webdriver.support.select import Select
select = Select(browser.find_element_by_name('depth1_1'))
select.select_by_index(1)

browser.find_element_by_xpath('/html/body/div[2]/div/div/form/table/tbody/tr[5]/td/div[2]/div[1]/ul/li[1]/label/span').click()

browser.find_element_by_xpath('/html/body/div[2]/div/div/form/table/tbody/tr[5]/td/div[3]/span/button').click()


# 날짜 정하기

# Click to open drop-down
date = browser.find_element_by_xpath("/html/body/div[2]/div/div/form/table/tbody/tr[8]/td[1]/label[1]/input").click()
# Choose depart date
wait(browser, 10).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[2]/div/div/form/table/tbody/tr[8]/td[1]/label[1]/input"))).click()
# Choose return date
wait(browser, 10).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[2]/div/div/form/table/tbody/tr[8]/td[1]/label[1]/input"))).click()




datefield = browser.find_element_by_id("frm-ReceiveStartYmd")
datefield.click()
browser.find_element_by_id('frm-receiveStartYmd').send_keys('2020.12.01')

datefield = browser.find_element_by_id("frm-ReceiveEndYmd")
datefield.click()
browser.find_element_by_id('frm-receiveEndYmd').send_keys('2020.12.31')







browser.find_element_by_xpath('/html/body/div[2]/div/div/form/table/tbody/tr[8]/td[2]/label[3]/input').click()  # 체크박스 클릭

browser.find_element_by_xpath('/html/body/div[2]/div/div/form/div[2]/button').click()  # [다음] 클릭