#! /usr/bin/env python3
# -*- encoding:utf-8 -*-
# version: 3.1.1
# author: Yexiaomo
# email: fxb1788@163.com
from bs4 import BeautifulSoup
import requests
import bs4
import re
'''
提取linklist.txt链接中的药物组成
不能处理的
        癫狗咬毒汤
        三物香薷饮
        骨灰固齿散
'''
def getHTMLText(url):
    try:
        session = requests.Session()
        session.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.63 Safari/537.36'
        }
        r = session.get(url)
        r.status_code
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "出现异常,爬取失败"
def processLine(line):
    url =  line.split('->')[1]
    # url = r'https://baike.baidu.com/item/%E5%85%AB%E7%8F%8D%E7%B3%95/6440974?fr=aladdin'
    htmlText = getHTMLText(url)
    soup = BeautifulSoup(htmlText, 'html.parser')
    rs = soup.find_all(class_='para')[2].text+"--"+soup.find_all(class_='para')[3].text
    print(line.split('->')[0]+':\n'+rs)
def main():
    linklisk = open("linklist2.txt", 'r', encoding='UTF-8')
    linkliskLines = linklisk.readlines()
    for line in linkliskLines:
        processLine(line.replace('\n',''))
    linklisk.close()
    
if __name__ == '__main__':
    main()