# 寻找优秀出版选题：
# 1.在豆瓣上搜寻评论数高、评分高的绝版书；
# 2.在知乎、雪球、简书上寻找优质作者。


# 1.在豆瓣上搜寻评论数高、评分高的绝版书；
from urllib.request import urlopen
from urllib.error import HTTPError, URLError
import requests
from bs4 import BeautifulSoup
import csv

csvFile = open("../subject_douban_search.csv", 'w+', newline='')
writer = csv.writer(csvFile)
writer.writerow(['书名', '作者名', '评分'])
session = requests.Session()
headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5)"
                        "AppleWebKit 537.36 (KHTML, like Gecko) Chrome",
           "Accept":"text/html,application/xhtml+xml,application/xml;"
                    "q=0.9,image/webp,*/*;q=0.8"}
def getNames(ProductList):
    try:
        url_origin = "https://book.douban.com/subject/" + ProductList + "/"
        html = urlopen(url_origin)
    except (HTTPError, URLError) as e:
        return ['找不到页面']
    try:
        bsObj = BeautifulSoup(html.read())
        BookName = bsObj.find("span", {"property": "v:itemreviewed"}).get_text()
        WriterName = bsObj.find("div", {"id": "info"}).findAll("a")
        if WriterName == []:
            WriterName = "不详"
        else:
            WriterName = WriterName[0].get_text().replace('\n            ', '').replace('    ', '')
        Score= bsObj.find("strong", {"property": "v:average"}).get_text()

    except AttributeError as e:
        return ['非图书详情页']
    return BookName, WriterName, Score, url_origin

for y in range(10391051, 10391055):
    writer.writerow(getNames(str(y)))
    print(getNames(str(y)), y)
