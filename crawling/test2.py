import requests
# import time, json , requests
# from django.http import  HttpResponse
from bs4 import BeautifulSoup
# import urllib, csv
# import pandas as pd # conda install pandas <= 설치되어 있음.
# import re
# from .models import exval
# from django.shortcuts import render
# import datetime
# import pandas


# str1 = requests.get(url).text # 문자열
# dic = json.loads(str1) #[{},{},{},{},{}]

def spider(max_pages):
    page = 1
    while page < max_pages:
        url = 'https://creativeworks.tistory.com/' + str(page)
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, 'lxml')
        for link in soup.select('h2 > a'):
            href = "http://creativeworks.tistory.com" + link.get('href')
            title = link.string
            print(href)
            print(title)
            
        page += 1

spider(2)
        