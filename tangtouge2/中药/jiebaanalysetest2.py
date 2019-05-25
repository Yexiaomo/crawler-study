#! /usr/bin/env python3
# -*- encoding:utf-8 -*-
# version: 1.10.25
# author: Yexiaom
# email: fxb1788@163.com
import jieba.analyse
txt = open("汤头歌.txt", 'r', encoding='UTF-8').read()
keywords = jieba.analyse.extract_tags(txt, topK=False, allowPOS='n')
print(keywords)