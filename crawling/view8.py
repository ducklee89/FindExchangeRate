import re
import requests as rq
from bs4 import BeautifulSoup
from selenium import webdriver
import json
import pandas as pd
import time

url = 'http://www.koreaexim.go.kr/site/program/financial/exchangeJSON?authkey=8WYTPowrz7mtIWE1yEP2VBPni7pVR1b8&searchdate=20020206&data=AP01'
driver = webdriver.Chrome('chromedriver')
driver.get(url)
soup = BeautifulSoup(driver.page_source)
print(soup.select('div'))



driver = webdriver.Chrome('chromedriver')
driver.get(url)





