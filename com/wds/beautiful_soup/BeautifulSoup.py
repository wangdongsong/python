# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup

def base_test(r):
    demo = r.text
    # 三种方式都可以
    soup = BeautifulSoup(demo, "html.parser")
    # soup = BeautifulSoup("<html>data</html>", "html.parser")
    # soup = BeautifulSoup(open("D:/demo.html"), "html.parser")
    print(soup.text)

    # 获取soup中的链接标签
    a_tag = soup.a
    print(a_tag)
    # a标签的父节点
    print(a_tag.parent.name)

    # a标签中的内容
    print(a_tag.string)
    print(type(a_tag.string))

    # 获取标签属性，JSON结构
    print(a_tag.attrs)
    a_tag_attrs = a_tag.attrs
    print(a_tag_attrs["href"])

    newsoup = BeautifulSoup("<b><!--title is comment--></b><p>This is not a comment</p>", "html.parser")
    print(newsoup.b.string)
    print(type(newsoup.b.string))
    print(newsoup.p.string)
    print(type(newsoup.p.string))

def sibling(soup):
    # 下行遍历
    print(soup.head)
    print(soup.body.contents)
    print(len(soup.body.contents))
    print(soup.body.contents[1])
    # 上行遍历
    for parent in soup.a.parents:
        if parent is None:
            print(parent)
        else:
            print(parent.name)
    # 平行遍历
    print(soup.a.next_sibling)
    # 后序节点
    print(soup.a.next_sibling.next_sibling)
    print(soup.a.previous_sibling)
    # 前序
    print(soup.a.previous_sibling.previous_sibling)

if __name__ == "__main__":
    r = requests.get("http://python123.io/ws/demo.html")
    #基本用法
    #base_test(r)
    soup = BeautifulSoup(r.text, "html.parser")
    #遍历
    #sibling(soup)
    print(soup.a.prettify())

