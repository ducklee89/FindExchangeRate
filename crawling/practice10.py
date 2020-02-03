import requests
from bs4 import BeautifulSoup as BS
from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
import selenium



# response = requests.get('https://www.kebhana.com/cont/mall/mall15/mall1501/index.jsp')

# print(response)
# print(response.text)

#응답 html코드를 text로 변환
# html = response.text

#응답받은 html코드를 BeautifulSoup에 사용하기 위하여 인스턴스 지정
# soup = BS(html, 'html.parser')
 
#원하는 태그 지정해서 출력
# for tag in soup.select('#searchContentDiv > div.printdiv > table > tbody > tr'):
#     #li[class=course]
#     print(tag.text)

# selenium 사용할 때
# driver = webdriver.Chrome('./chromedriver.exe')
# driver.implicitly_wait(3)

# driver.get('https://https://www.kebhana.com/cont/mall/mall15/mall1501/index.jsp')
# driver.get('https://google.com')


# 아이디/비밀번호를 입력해준다.
# driver.find_element_by_name('id').send_keys('naver_id')
# driver.find_element_by_name('pw').send_keys('mypassword1234')
#url에 접근한다.

# id = ''
# pw= ''

# driver.execute_script("document.getElementsByName('id')[0].value=\'"+id+"\'")
# driver.execute_script("document.getElementsByName('pw')[0].value=\'"+pw+"\'")
# time.sleep(0.5)

# driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input').click()
# time.sleep(1)
# driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/span[1]/a').click()
# time.sleep(1)
# driver.find_element_by_xpath('//*[@id="login_maintain"]/span[1]').click()
# time.sleep(1)


# def exchange_Crawling(html):
#     exchange_list = []
 
#     tr_list = html.select('#searchContentDiv > div.printdiv > table > tbody > tr')
 
#     for tr in tr_list :
#         rank = int(tr.find('td',{'class':'tc'}).find('span').text.strip('환율'))
 
#         img = tr.find('td',{'class':'tc'}).find('div',{'class':'txtAr'}).find('img')['src']
#         img = tr.find('td',{'class':'tc'}).find('div',{'class':'txtAr'}).find('img').get('src')
 
#         title = tr.find('td',{'class':'tc'}).find('div',{'class':'txtAr'}).find('a',{'class':'txtAr'}).text
#         artist = tr.find('td',{'class':'tc'}).find('div',{'class':'txtAr'}).find('a',{'class':'txtAr'}).text
#         album = tr.find('td',{'class':'tc'}).find('div',{'class':'txtAr'}).find('a',{'class':'txtAr'}).text
#         exchange_list.append([no, title, content, artist, album])
 
 
 
#     return exchange_list
# #============================================================ End of mnet_Crawling() ============================================================#
 
# exchange1_list = []
 
# req = requests.get('https://www.kebhana.com/cont/mall/mall15/mall1501/index.jsp')
 
# for page in [1,2]:
#     req = requests.get('https://www.kebhana.com/cont/mall/mall15/mall1501/index.jsp'.format(page))

#     html = BS(req.text, 'html.parser')
#     print(html)
    
#     # exchange1_list += exchange1_Crawling(html)
#     # pass

 
 
# # 리스트 출력
# for item in exchange1_list :
#     print(item)