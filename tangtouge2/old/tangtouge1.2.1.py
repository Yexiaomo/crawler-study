#! /usr/bin/env python3
# -*- encoding:utf-8 -*-
# version: 1.2.1
# author: Yexiaomo
# email: fxb1788@163.com
'''
尝试使用jieba词库对文本进行初步分词
1.并查看分词结果
2.统计词频
'''
import jieba
import re

#对文本的每一行计算词频
def processLine(line, wordCounts):
    words = jieba.lcut(line, cut_all=True, )
    words.remove('')
    words.remove('')
    # words = jieba.lcut(line, cut_all=False)
    # words.remove(' ')
    words.pop()
    #从每一行获取每个词
    for word in words:
        if word in wordCounts:
            wordCounts[word] += 1
        else:
            wordCounts[word] = 1

def main():

    tangtouge = open("汤头歌.txt", 'r', encoding='UTF-8')
    tangtougeLines = tangtouge.readlines()

    #用于计算词频的空字典
    wordCounts = {}
    for line in tangtougeLines:
        line.replace('\n', '')
        if (re.search('[/d.、：]|增辑', line)):
            continue
        processLine(line, wordCounts)
    #从字典中获取数据对
    pairs = list(wordCounts.items())
    #列表中的数据对 交换位置,数据对排序
    items = [[x,y] for (y,x)in pairs]
    items.sort()
    #输出词频结果
    for i in range(len(items)):
        print( items[i][1] + '\t' + str(items[i][0]))
    print('---end---')
    print(items[len(items)-1])
    tangtouge.close()

if __name__ == '__main__':
    main()