

import os
import requests

def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        print(r.url)
        #print(r.content)
        return r.text
    except:
        return "system exception"

def getJD(url):
    r = requests.get("https://item.jd.com/2967929.html")
    print(r.status_code, r.encoding, r.apparent_encoding)
    print(r.text)

def get_amazon(url):
    #亚马逊屏幕了user-agent为*的请求，所以需要修改请求头的user-agent
    try:
        kv = {"user-agent": "Mozilla/5.0"}
        r = requests.get(url, headers=kv)
        r.raise_for_status()
        print(r.status_code, r.encoding, r.apparent_encoding)
        r.encoding = r.apparent_encoding
        print(r.url)
        #print(r.content)
        return r.text
    except:
        return "system exception"

def get_keyword_baidu(url):
    try:
        kv = {"wd" : "python"}
        r = requests.get(url, params = kv)
        r.raise_for_status()
        print(len(r.text))
        print(r.request.url)
    except:
        return "system exception"

def get_pic(url):
    root_path = "E:/javaTest/"
    print(url.split("/"))
    path = root_path + url.split("/")[-1]
    try:
        if not os.path.exists(root_path):
            os.mkdir(root_path)
        if not os.path.exists(path):
            r = requests.get(url)
            r.raise_for_status()
            with open(path, "wb") as f:
                f.write(r.content)
                f.close()
                print("file save success")
    except:
        return "system exception"


def get_src_ip(ip):
    try:
        r = requests.get("http://m.ip138.com/ip.asp?ip=" + ip)
        r.raise_for_status()
        print(r.text)
    except:
        return "system exception"

if __name__ == "__main__":
    #result = getHTMLText("http://www.baidu.com")
    #print(result)
    #getJD("")
    #get_amazon("https://www.amazon.cn/gp/product/B01M8L5Z3Y")
    #get_keyword_baidu("http://www.baidu.com/s")
    #get_pic("http://p2.ifengimg.com/a/2017_10/30af5f1a3a56f93_size32_w550_h418.png")
    get_src_ip("202.204.80.11")



