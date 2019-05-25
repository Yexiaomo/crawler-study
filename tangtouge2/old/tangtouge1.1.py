#! /usr/bin/env python3
# -*- encoding:utf-8 -*-
# version: 1.1
# author: Yexiaomo
# email: fxb1788@163.com
'''
初步接触jieba分词词库
1.了解全模式,精确模式,搜索模式的区别
2.尝试运行查看效果
'''
import jieba

txt = open("汤头歌.txt", 'r', encoding='UTF-8').read()
seg_list = jieba.cut(txt, cut_all=False)
print(type(seg_list))
print("Full Mode: " + " ".join(seg_list))  # 全模式