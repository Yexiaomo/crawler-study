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
保存结果生成linklist.txt
不能处理的
        癫狗咬毒汤
        三物香薷饮
        骨灰固齿散
'''

infile = open("linklist.txt", 'w', encoding='UTF-8')
def getHTMLText(url):
    try:
        r = requests.get(url)
        r.status_code
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "出现异常,爬取失败"
def SearchResult(keyword):
    url = 'http://www.baidu.com/s?wd='+keyword
    if (keyword=='藿香正气散'):
        url = url+' 百度百科'
    searchHtmlText = getHTMLText(url)
    searchsoup = BeautifulSoup(searchHtmlText, 'html.parser')
    # 这一步直接得到百度百科对关键字的链接
    serachlinklist = searchsoup.find(class_="t c-gap-bottom-small").find('a').get('href')
    # 对搜索到的链接进行存储
    infile.write(keyword+'->'+serachlinklist+'\n')
def processLine(line):
    if (re.search("\.", line)):
        keyword =  line.split('.')[1]
        return SearchResult(keyword)
    else:
        return ''
def main():
    tangtouge = open("汤头歌标题.txt", 'r', encoding='UTF-8')
    tangtougeLines = tangtouge.readlines()
    for line in tangtougeLines:
        processLine(line)
    tangtouge.close()
    
if __name__ == '__main__':
    main()
infile.close()