# encoding: utf-8
'''
Created on 2018年3月23日

@author: wangs0622

question: 剑指 offer 17 题，打印从 1 到最大的 n 位数
输入的数字为 n，按顺序打印从 1 到最大的 n 位十进制数。
'''

from collections import deque
def printAllNumber(N):
    '''
    : 我自己写的程序，用列表来表示每一个元素
    '''
    if N <= 0: return 
    number_list = deque([0])
    while len(number_list) <= N:
        number_list[-1] += 1
        i = -1
        while number_list[i] == 10:
            if i == -len(number_list):
                number_list[i] = 0 
                number_list.appendleft(1)
            else:
                number_list[i] = 0
                number_list[i-1] += 1
            i -= 1
        str_number = ''.join([str(num) for num in number_list])
        if len(str_number) <= N: print(str_number)
        
#----------------------------------------------------------------------
# 按照书上所说写的，但是由于 python 中的字符串是不可变的，所以用列表代替   
def printToMaxOfNDigits(n):
    if n <= 0: return 
    number = [0]*n
    for i in range(10):
        number[0] = i
        printToMaxOfNDigitsRecursively(number, n, 0)

def printToMaxOfNDigitsRecursively(number, n, index):
    if index == n - 1:
        printNumber(number)
        return
    for i in range(10):
        number[index+1] = i
        printToMaxOfNDigitsRecursively(number, n, index+1)
def printNumber(number):
    i = 0
    while i < len(number) and number[i] == 0 :
        i += 1
    if i != len(number):    
        print(''.join([str(num) for num in number[i:]]))

if __name__ == '__main__':
    printToMaxOfNDigits(2)
