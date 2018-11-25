# 寻找优秀出版选题：
# 1.在豆瓣上搜寻评论数高、评分高的绝版书；
# 2.在知乎、雪球、简书上寻找优质作者。


# 1.在豆瓣上搜寻评论数高、评分高的绝版书；
from urllib.request import urlopen
from urllib.error import HTTPError, URLError
from bs4 import BeautifulSoup
import csv
csvFile = open("../subject_douban_search.csv", 'w+', newline='')
writer = csv.writer(csvFile)
writer.writerow(['书名', '作者名', '评分'])
def getNames(ProductList):
    try:
        html = urlopen("https://book.douban.com/subject/"+ProductList+"/")
    except (HTTPError, URLError) as e:
        return ['找不到页面']
    try:
        bsObj = BeautifulSoup(html.read())
        BookName = bsObj.find("span", {"property": "v:itemreviewed"}).get_text()
        WriterName = bsObj.find("div", {"id": "info"}).findAll("a")
        Score= bsObj.find("strong", {"property": "v:average"}).get_text()

    except AttributeError as e:
        return ['非图书详情页']
    return BookName, WriterName[0].get_text().replace('\n            ', '').replace('    ', ''), Score

for y in range(1039300, 1039313):
    writer.writerow(getNames(str(y)))
    print(getNames(str(y)), y)
