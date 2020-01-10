#!/usr/bin/env python
# encoding: utf-8
'''
@author: liuchang
@time: 2020/1/10 10:17 上午
@comments: 学习Python输入流和输出流重定向
@link: https://blog.csdn.net/HUALUO003/article/details/89641563
'''

import sys

sys.stdout.write('uhhshdfsdds' + '\t')
sys.stdout.write("safdffsewr" + '\n')
sys.stdout.write('dsdsewerfg' + '\n')
print('--------------')

oneLine = sys.stdin.readline()
print(oneLine)
print(len(oneLine))

oneLine = oneLine.strip('\n')
print(oneLine)
print(len(oneLine))
print('---------------')

text = sys.stdin.readlines() # 按Ctrl+D结束输入
print(text)

list1 = []
for line in text:
    line1 = line.strip('\n')
    list1.append(line1)
print(list1)
print('-----------------')


# 按下ctrl+D之后不能再次使用sys.stdin.readline()和sys.stdin.readlines()
# text2 = sys.stdin.readlines()
# print(text2)

# stdout重定向到文件
console = sys.stdout
file = open("data.txt", 'w')
sys.stdout = file
print('hello\n' + 'java\n' + 'python')
sys.stdout = console
print(3333)

# stdin重定向到文件,在cmd输入语句
# python ***.py < filepath

# stdin重定向到文件
console = sys.stdin
file = open("data.txt", 'r')
sys.stdin = file
content = input()
content2 = sys.stdin.readlines()
file.close()
print(content) # 输入一行，不包含回车换行符
print(content2) # 输入其余内容，包含回车换行符，遇到文件尾自动结束输入
sys.stdin = console # 恢复定向