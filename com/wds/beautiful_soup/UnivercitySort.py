# -*- coding: utf-8 -*-

import requests
import bs4
from bs4 import BeautifulSoup


def get_html_text(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""


def fill_univ_list(ulist, html):
    soup = BeautifulSoup(html, "html.parser")
    for tr in soup.find("tbody").children:
        if isinstance(tr, bs4.element.Tag):
            tds = tr("td")
            ulist.append([tds[0].string, tds[1].string, tds[2].string])


def print_univ_list(ulist, num):
    template = "{0:^10}\t{1:{3}^10}\t{2:^10}"
    print(template.format("排名", "学校名称", "地区", chr(12288)))
    for i in range(num):
        u = ulist[i]
        print(template.format(u[0], u[1], u[2], chr(12288)))


if __name__ == "__main__":
    uinfo = []
    url = "http://www.zuihaodaxue.cn/zuihaodaxuepaiming2016.html"
    html = get_html_text(url)
    fill_univ_list(uinfo, html)
    print_univ_list(uinfo, 10)
