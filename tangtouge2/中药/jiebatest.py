#! /usr/bin/env python3
# -*- encoding:utf-8 -*-
# version: 1.10.25
# author: Yexiaom
# email: fxb1788@163.com
# import jieba.analyse
# txt = open("汤头歌.txt", 'r', encoding='UTF-8').read()
# allowPosTup = ('n', 'nb', 'nba', 'nbc', 'nbp', 'nf', 'ng', 'nh', 'nhd', 'nhm', 'ni', 'nic', 'nis', 'nit', 'nl', 'nm', 'nmc', 'nn', 'nnd', 'nnt', 'nr', 'nr1', 'nr2', 'nrf', 'nrj', 'ns', 'nsf', 'nt', 'ntc', 'ntcb', 'ntcf', 'ntch', 'nth', 'nto', 'nts', 'ntu', 'nx', 'nz')
# for i in range(len(allowPosTup)):
#     keywords = jieba.analyse.extract_tags(txt, topK=False, allowPOS=allowPosTup[i])
#     filename = '%s.%s'%(allowPosTup[i],'txt')
#     f = open(filename, 'w', encoding="utf-8")
#     f.write(str(keywords))
#     f.close()