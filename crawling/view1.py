import requests
from bs4 import BeautifulSoup 


def main():


    html_url = "https://www.kebhana.com/cont/mall/mall15/mall1501/index.jsp" 

    r = requests.get(html_url) #bs = BeautifulSoup(r.text, 'html.parser') 
    bs = BeautifulSoup(r.text, 'lxml') #기본 파서
    
    #print(bs.prettify())


    for tr in bs.find_all('tr'):
        print(tr.prettify()) #lxml 파서 # li 엘리먼트 검색


    tr = bs.find("tr", class_="tc")
    for td1 in tr.find_all("tr"):
        print(td1.prettify())



if __name__ == '__main__':
    main()