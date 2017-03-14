# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import re #正则表达式引入

if __name__ == "__main__":
    r = requests.get("http://python123.io/ws/demo.html")
    soup = BeautifulSoup(r.text, "html.parser")

    #下面两行代码结果相同
    print(soup("p", "course"))
    print(soup.find_all("p", "course"))

    #所有a标签
    for link in soup.find_all("a"):
        print(link.get("href"))

    #查询所有标签
    for tag in soup.find_all(True):
        print(tag.name)

    for tag in soup.find_all(re.compile("b")):
        print(tag.name)

    for tag in soup.find_all("p", "course"):
        print(tag)

    print(soup.find_all(id="link1"))

    print(soup.find_all(id=re.compile("link")))

    #文本内容包括Basic Python
    print(soup.find_all(string = "Basic Python"))

    #所有Python字符
    print(soup.find_all(string = re.compile("python")))