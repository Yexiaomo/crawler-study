#! /usr/bin/env python3
# -*- encoding:utf-8 -*-
# version: 2.2.1
# author: Yexiaomo
# email: fxb1788@163.com
import jieba.analyse
import re
'''
对jieba.analyse进一步精确对文本进行分词
对比 精确分词和分析模式下的区别
查看运行结果,进行保存对比
'''
#对文本的每一行计算词频
def processLine(line):
    if (re.search('[/d.、：]|增辑', line)):
        return False
    else:
        allowPosTup = ('n', 'nb', 'nba', 'nbc', 'nbp', 'nf', 'ng', 'nh', 'nhd', 'nhm', 'ni', 'nic', 'nis', 'nit', 'nl', 'nm', 'nmc', 'nn', 'nnd', 'nnt', 'nr', 'nr1', 'nr2', 'nrf', 'nrj', 'ns', 'nsf', 'nt', 'ntc', 'ntcb', 'ntcf', 'ntch', 'nth', 'nto', 'nts', 'ntu', 'nx', 'nz')
        words = jieba.analyse.extract_tags(line, topK=False, allowPOS=allowPosTup)
        return str(words)
def main():
    tangtouge = open("汤头歌.txt", 'r', encoding='UTF-8')
    infile = open("分词汤头歌.txt", 'w', encoding='UTF-8')
    tangtougeLines = tangtouge.readlines()
    cntlines = 0
    for line in tangtougeLines:
        if(processLine(line) == False):
            infile.write(line)
        else:
            infile.write(line.replace('\n','')+"-->"+processLine(line)+'\n')
    tangtouge.close()
    infile.close()

if __name__ == '__main__':
    main()