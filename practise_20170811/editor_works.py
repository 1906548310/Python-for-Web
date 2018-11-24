# Mike每天的例行工作内容：
# 1.查看自己的书出版情况（京东当当的排名、评论数、库存、近期发书、退书）；
# 2.查看最近举办哪些有用的会议（活动行等）；
# 3.查看京东的经管图书新书榜、所有图书新书总榜前100本图书。


# 寻找优秀出版选题：
# 1.在豆瓣上搜寻评论数高、评分高的绝版书；
# 2.在知乎、雪球、简书上寻找优质作者。


# http://book.jd.com/booktop/0-1-0.html?category=20003-0-1-0-10001-1
# http://book.jd.com/booktop/0-1-0.html?category=20003-0-1-0-10001-2

# 爬京东经管新书榜前100名图书
from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv
# csvFile = open("../../../../../E215Gu/desktop/JD_jg_top100.csv", 'w+')  #如果让行与行之间没有空行，就加上：, newline=''
csvFile = open("../JD_jg_top100.txt", 'w+')

nameList = []
for m in range(5):
    url = "http://book.jd.com/booktop/0-1-0.html?category=20003-0-1-0-10001-" + str(m+1)
    html = urlopen(url)
    bsObj = BeautifulSoup(html.read())
    nameList = nameList + bsObj.findAll('a',{'class':{'p-name'}})

try:
    writer = csv.writer(csvFile)
    writer.writerow(['京东经管类新书前100名'])
    n = 1
    for i in nameList:
        writer.writerow((n, i.get_text()))
        n = n + 1
finally:
    csvFile.close()
