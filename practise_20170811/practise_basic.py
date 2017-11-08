# # 条件判断
# print("Hello World,","I'm your AI.")
# name = input("请告诉我，你的名字：")
# if name == "Mike":
#     print("Hello, Mike.")
# elif name == 'guqiang':
#     print("Anything I can do for you, my Lord?")
# else:
#     print("Sorry, I don't know someone called " + name + ".")

# # 循环语句
# print(list(range(101)))
# sum = 0
# for x in range(101):
#     sum = sum + x
# print(sum)
#
# sum_while = 0
# n =0
# while n < 101:
#     sum_while = sum_while + n
#     n = n + 1
# print(sum_while)

# print(ord('A'))
# print(chr(66))
# print(ord('总'))

# # Python还有list数据类型
# classmate = ['LiLei','HanMeiMei','SingleDog']
# print(classmate)
# print(len(classmate))
# print(classmate[len(classmate)-1])
# print(classmate[-1])
# classmate.append('John')
# print(classmate)
# classmate.insert(1,'Stark')
# print(classmate)
# classmate.pop(0)
# print(classmate)
# # tuple数据类型
# classname = ('num_01',315,True)
# print(classname)
# classname_01 = (1,)
# print(classname_01)

# # dict，有点类似于JS的对象
# Starks = {'Rob':26,'John':25,'Sansa':23,'Aya':20}
# print(Starks['John'])
# print('Sam' in Starks)
# print(Starks.get('Joffrey',-2))
# # 删去‘Rob’的键-值
# Starks.pop('Rob')
# print(Starks)

# # set，类似于dict，无序，无重复
# example_set = set([1,2,3,3,4,5,5])
# print(example_set) #输出{1, 2, 3, 4, 5}
# example_set.add(1)
# print(example_set) #输出{1, 2, 3, 4, 5}
# example_set.remove(2)
# print(example_set) # 输出{1, 3, 4, 5}
# example_compare = set([4,5,6])
# print(example_set & example_compare) #求交集
# print(example_set | example_compare) #求并集

# # Python函数
# def import_message(name,age,city='北京',nation='中国'): #city和nation为默认参数
#     print('我来自' + nation + '的' + city + '，' + '我叫' + name + '，' + '今年' + age + '岁。')
# import_message('Mike','25')
# import_message('Sansa','23','Winterfall','Westerol')
#
# def calc(*numbers): #可变参数的应用，计算a平方 + b平方 + c平方 + ……
#     sum = 0;
#     for n in numbers:
#         sum = sum + n*n
#     return sum
# print(calc(1,2,3,4,5))
#
# def keyword(name,age,**other):
#     print('name:',name,'age:',age,'other:',other)
# keyword('Mike','25',city='北京',nation='中国')

# # 切片——针对list、tuple、string管用
# example_slice_list = [1,3,5,7,9,11]
# print(example_slice_list[0:3])
# example_slice_tuple = (2,4,6,8,10)
# print(example_slice_tuple[1:4])
# example_list = list(range(100))
# print(example_list)
# #切最后面10个数
# print(example_list[-10:])
# #每隔1个切出来
# print(example_list[::2])
# #完整复制
# print(example_list[:])

# # 迭代
# Starks = {'Rob':26,'John':25,'Sansa':23,'Aya':20,'Brandon':18,'Rickon':16}
# for key in Starks:
#     print(key)
# for value in Starks.values():
#     print(value)
# for k,v in Starks.items():
#     print(k,v)
#
# # 判断一个对象是否是可迭代对象，通过collections模块的Iterable类型判断
# from collections import Iterable
# print(isinstance(Starks,Iterable))
# print(isinstance('abcde',Iterable))
# print(isinstance([1,2,3,4,5],Iterable))
# print(isinstance(12345,Iterable))
#
# # enumerate函数可以将list变成索引-元素对
# for i,value in enumerate(['A','B','C']):
#     print(i,value)
#
# for x,y in [(1,1),(2,4),(3,6)]:
#     print(x,y)

# # 列表生成式
# print(list(range(1,11)))
# print([x*x for x in range(1,11)])
# print([x for x in range(1,11) if x%2 == 0])
# print([m+n for m in 'ABC' for n in 'CDE'])

# #生成器
# G = (x*x for x in range(11)) #G就是一个简单的生成器
# print(G)  #打印G的真面目：<generator object <genexpr> at 0x0000000002119888>
# for y in G:
#     print(y)  #利用For循环打印生成器生成的每个结果

# def feiboraki(max):
#     n,a,b = 0,0,1
#     while(n < max):
#         yield b
#         a,b = b,a+b
#         n = n+1
#     return "done"
#
# o = feiboraki(6)
# print(o)
#
# for x in o:
#     print(x)

# import this #可以看到发明python语言大神的箴言


# # 验证BeautifulSoup安装成功
# from bs4 import BeautifulSoup

# # 防止爬虫爬取数据时出错中断，从而采取的抛出错误解决办法（try……except……）*****
# from urllib.request import urlopen
# from urllib.error import HTTPError, URLError
# from bs4 import BeautifulSoup
# def getTitle(url):
#     try:
#         html = urlopen(url)
#     except (HTTPError, URLError) as e:
#         return None
#     try:
#         bsObj = BeautifulSoup(html.read())
#         title = bsObj.body.h1
#     except AttributeError as e:
#         return None
#     return title
# title = getTitle("https://1906548310.github.io/index.html")
# if title == None:
#     print("Title could not be found")
# else:
#     print(title)


# from urllib.request import urlopen
# from urllib.error import HTTPError, URLError
# from bs4 import BeautifulSoup
# html = urlopen("https://1906548310.github.io/index.html")
# bsObj = BeautifulSoup(html.read())
# nameList = bsObj.findAll('h4',{'class':{'pull-left','pull-right'}})
# hhh = bsObj.findAll({'h3','h4','h5'})
# print(hhh)
# for i in nameList:
#     print(i.get_text())


## 下面的代码就是获取有两个属性的标签：
## soup.findAll(lambda tag: len(tag.attrs) == 2)
## 这行代码会找出下面的标签：
## <div class="body" id="content"></div>
## <span style="color:red" class="title"></span>



# Scrapy 就是一个帮你大幅度降低网页链接查找和识别工作复杂度的Python 库，它可以
# 让你轻松地采集一个或多个域名的信息。不过目前Scrapy 仅支持Python 2.7，还不支持
# Python 3.x。



# from urllib.request import urlopen
# from bs4 import BeautifulSoup
# import re #使用正则？
# NameList = []
# BookName = ""
# def getNames(ProductList):
#     html = urlopen("https://item.jd.com/"+ProductList+".html")
#     bsObj = BeautifulSoup(html)
#     catlog = bsObj.find("div", {"class":"breadcrumb"}).findAll("a", {"clstag":"shangpin|keycount|product|mbNav-2"})
#
#     for x in catlog:
#         BookName = x.get_text()
#
#     if BookName == "科普读物":
#         return bsObj.find("div", {"id":"name"}).findAll("h1")
#     else:
#         return []
#
# for y in range(12100000, 12200000):
#     NameList += getNames(str(y))
#
# for z in NameList:
#     print(z.get_text())


from urllib.request import urlopen
from urllib.error import HTTPError, URLError
from bs4 import BeautifulSoup
NameList = []
# BookName = ""
def getNames(ProductList):
    try:
        html = urlopen("https://item.jd.com/"+ProductList+".html")
    except (HTTPError, URLError) as e:
        return ['非页面']
    try:
        bsObj = BeautifulSoup(html.read())
        catlog = bsObj.find("div", {"class": "breadcrumb"}).findAll("a", {"clstag": "shangpin|keycount|product|mbNav-2"})

        for x in catlog:
            BookName = x.get_text()

        if BookName == "科普读物":
            title = bsObj.find("div", {"id":"name"}).findAll("h1")
        else:
            return ['非科普']

    except AttributeError as e:
        return ['非图书']
    return title

for y in range(12143691, 12226949):
    print(getNames(str(y)))
    print(y)

# for z in NameList:
#     print(z.get_text())















