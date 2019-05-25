import re
import jieba
import jieba.analyse
#! /usr/bin/env python3
# -*- encoding:utf-8 -*-
# version: 3.2.1
# author: Yexiaomo
# email: fxb1788@163.com
jieba.load_userdict('tangtouge_add_words.txt')
jieba.analyse.set_stop_words('tangtouge_stop_words.txt')
def processLine(line):
    if (re.search('[/d.、：]|增辑', line)):
        return ''
    else:
        allowPosTup = ('n', 'nb', 'nba', 'nbc', 'nbp', 'nf', 'ng', 'nh', 'nhd', 'nhm', 'ni', 'nic', 'nis', 'nit', 'nl', 'nm', 'nmc', 'nn', 'nnd', 'nnt', 'nr', 'nr1', 'nr2', 'nrf', 'nrj', 'ns', 'nsf', 'nt', 'ntc', 'ntcb', 'ntcf', 'ntch', 'nth', 'nto', 'nts', 'ntu', 'nx', 'nz')
        analyseswords = jieba.analyse.extract_tags(line, topK=False, allowPOS=allowPosTup)
        words = ' '.join(jieba.lcut(' '.join(analyseswords)))
        words = re.sub(' +',' ', words)
        return (words)
def main():
    tangtouge = open("汤头歌.txt", 'r', encoding='UTF-8')
    infile = open("分词汤头歌3.2.1.txt", 'w', encoding='UTF-8')
    tangtougeLines = tangtouge.readlines()
    for line in tangtougeLines:
        if(processLine(line) == ''):
            print(line)
        else:
            print(line.replace('\n','')+"-->"+str(processLine(line).split())+'\n')
    tangtouge.close()
    infile.close()

if __name__ == '__main__':
    jieba.suggest_freq(('参','术'), True)
    jieba.suggest_freq(('柴','半知'), True)
    main()