#!/usr/bin/env python
# encoding: utf-8
'''
@author: liuchang
@software: PyCharm
@file: leetcode17.py
@time: 2020-03-24 11:08
如果数组中多一半的数都是同一个，则称之为主要元素。给定一个整数数组，找到它的主要元素。若没有，返回-1。
'''


class Solution:
    def majorityElement(self, nums):
        ndict = {}
        for e in nums:
            if e in ndict.keys():
                ndict[e] += 1
            else:
                ndict[e] = 1
        nlen = len(nums)
        for k in ndict.keys():
            if ndict[k] > nlen/2:
                return k
        return -1

if __name__ == '__main__':
    oc = Solution()
    res = oc.majorityElement([2,3])
    print(res)

