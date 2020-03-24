#!/usr/bin/env python
# encoding: utf-8
'''
@author: liuchang
@software: PyCharm
@file: leetcode205.py
@time: 2020-03-24 17:35
#给定两个字符串 s 和 t，判断它们是否是同构的。
'''

class Solution:
    def isIsomorphic(self, s, t):
        ndict = {}
        for i in range(len(s)):
            if s[i] not in ndict.keys() and t[i] not in ndict.values():
                ndict[s[i]] = t[i]
        n = ""
        for i in range(len(s)):
            try:
                n += ndict[s[i]]
            except:
                return False

        if n == t:
            return True
        else:
            return False


if __name__ == '__main__':
    s = Solution()
    res = s.isIsomorphic("paper","title")
    print(res)