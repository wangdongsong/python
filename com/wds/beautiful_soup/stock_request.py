import requests
from bs4 import BeautifulSoup
import bs4
import traceback
import re


def get_html_text(url, encoding="utf-8"):
    try:
        r = requests.get(url, timeout = 30)
        r.raise_for_status()
        #r.encoding = r.apparent_encoding
        r.encoding = encoding
        return r.text
    except:
        return ""


def get_stock_list(lst, stock_url):
    html = get_html_text(stock_url, "GB2312")
    soup = BeautifulSoup(html, "html.parser")
    a = soup.find_all("a")
    #print(a)
    for i in a:
        try:
            #print(i)
            #print(type(i[0]))
            href = i.attrs["href"]
            #print(re.findall(r"[s][hz]\d{6}", href)[0])
            stock_code = re.findall(r"[s][hz]\d{6}", href)
            #print(stock_code)
            #print(len(stock_code))
            if(len(stock_code) > 0):
                lst.append(stock_code[0])
        except:
            traceback.print_exc()
            continue
    #return lst

def get_stock_info(lst, stock_url, fpath):

    print(len(lst))
    count = 0
    for stock in lst:
        count = count + 1
        #if(count == 30):
         #   break
        print(count)
        url = stock_url + stock + ".html"
        html = get_html_text(url)
        try:
            if html == "":
                continue
            else:
                info_dict = {}
                soup = BeautifulSoup(html, "html.parser")
                stock_info = soup.find("div", attrs={"class": "stock-bets"})
                #print(type(stock_info))

                if(type(stock_info) == type(None)):
                    print(type(stock_info))
                    print(type(stock_info) == type(None))
                    continue
                key_list = stock_info.find_all("dt")
                value_list = stock_info.find_all("dd")
                if(len(key_list) > 0):
                    name = stock_info.find_all(attrs={"class": "bets-name"})[0]
                    info_dict.update({"股票名称": name.text.split()[0]})
                    for i in range(len(key_list)):
                        key = key_list[i].text
                        val = value_list[i].text
                        info_dict[key] = val.replace("\n", "").replace(" ", "")
                    with open(fpath, "a", encoding="utf-8") as f:
                        f.write(str(info_dict) + "\n")
        except:
            traceback.print_exc()
            continue

    print("close")

if __name__ == '__main__':
    stock_list_url = "http://quote.eastmoney.com/stocklist.html"
    stock_info_url = "https://gupiao.baidu.com/stock/"
    output_file = "E:\javaTest\stock.txt"
    slist = []
    get_stock_list(slist, stock_list_url)
    #print(slist)
    get_stock_info(slist, stock_info_url, output_file)