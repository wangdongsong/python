


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

if __name__ == "__main__":
    result = getHTMLText("http://www.baidu.com")
    print(result)
