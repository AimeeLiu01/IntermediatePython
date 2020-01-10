#!/usr/bin/env python
# encoding: utf-8
'''
@author: liuchang
@time: 2020/1/10 11:10 上午
@comments: python 字符串(str)与列表(list)以及数组(array)之间的转换方法详细整理
@Link: https://blog.csdn.net/FrankieHello/article/details/80766439
'''

"""
在转换之前先研究一下python中list和array的不同。
1、list是python中内置的数据类型，其中的数据的类型可以不相同，array中的数据类型必须是一样的。
2、list中保存的数据的存放地址，而不是数据，会增加内存的占用，所以存放数据还是尽量使用array。
3、list中有append的方法，可以进行追加，而array没有追加的方法，只能通过np.append来实现追加。
4、在print的时候，打印的结果不同。list元素之间有","分割，而array之间是空格。
"""
import numpy as np
import pandas as pd

# 1. 首先区分list和arr, 其中，list和arr都可以通过取下标的形式获取数据
list = [1, 2, 3, 4]
arr = np.array(list)
print(list)
print(list[0])
print(arr)
print(arr[1])

# 2. list转换为str
# 当list中存放的数据是字符串时，一般是通过str中的join函数来进行转换
list = ['a','b','c','d']
str1 = ''.join(list)
str2 = " ".join(list)
str3 = '.'.join(list)
print(str1)
print(str2)
print(str3)

# 当list中存放的数据是整型数据或者数字的话，需要先将数据转换为字符串再进行转换
list = [1,2,3,4]
str1 = ''.join([str(x) for x in list])
str2 = ' '.join([str(x) for x in list])
str3 = '.'.join([str(x) for x in list])
print(str1)
print(str2)
print(str3)

# 3. array转为str
# 将array转换为str和list转换时是一样的，join()函数中的参数是一个iterator，所以array或者list都可以。
list = ['a','v','c','d']
arr = np.array(list)
str = ''.join(arr)
print(str)

# 4. str转换为list
# 这个str转list很有用，因为有很多字符串，可以通过转化为list的形式来取数
str1 = 'abcde'
str2 = 'a b c d e'
str3 = 'a,b,c,d,e'
#result1 = list(str1)
result2 = str2.split()
result3 = str3.split(',')
#print(result1)
print(result2)
print(result3)

str4 = '/Company/fadf7db7db670dd0fa2dfa00227bf8cd'
result4 = str4.split('/')
print("result4: ", result4) # result4:  ['', 'Company', 'fadf7db7db670dd0fa2dfa00227bf8cd']
print(result4[1]) # Company
print(result4[2]) # fadf7db7db670dd0fa2dfa00227bf8cd
