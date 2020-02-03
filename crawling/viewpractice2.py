import bs4
import urllib.request

url="https://www.kebhana.com/cont/mall/mall15/mall1501/index.jsp"
html = urllib.request.urlopen(url)


bs0bj = bs4.BeautifulSoup(html, "html.parser")
# print(bs0bj)
print(bs0bj.find("div"))
# print(html.read())

top_right = bs0bj.find("div", {"class":"area_links"})
print(top_right)
first_a = top_right.find("a")
print(first_a.text)


# html_str = "<html><div></div></html>"
# bs0bj = bs4.BeautifulSoup(html_str, "html.parser")

# print(type(bs0bj))
# print(bs0bj)
# print(bs0bj.find("div"))