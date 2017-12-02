# _*_ encoding:utf-8 _*_

'''
Created on 2017\11\29

@author: wangs0622
'''

import sort
import random
import matplotlib.pyplot as plt

def selectionSort(data):
    compare_num = 0
    exch_num = 0
    
    for i in range(len(data)):
        min_index = i
        for j in range(i,len(data)):
            compare_num += 1
            if data[j] < data[min_index]: 
                min_index = j
        sort.exch(data, i, min_index)
        exch_num += 1
        
    return compare_num, exch_num
        
def insertionSort(data):
    compare_num = 0
    exch_num = 0
    
    for i in range(1, len(data)):
        temp = range(i)
        temp.reverse()
        for j in temp:
            compare_num += 1
            if data[j+1] < data[j]:
                sort.exch(data, j, j+1)
                exch_num += 1
            else: 
                break
    return compare_num, exch_num

def bubbleSort(data):
    compare_num = 0
    exch_num = 0
    
    for i in range(len(data)-1):
        for j in range(len(data)-i-1):
            compare_num += 1
            if data[j] > data[j+1]:
                sort.exch(data, j, j+1)
                exch_num += 1
                
    return compare_num, exch_num

def shellSort(data):
    compare_num = 0
    exch_num = 0
    
    N = len(data)
    h = 1
    while(h < N/3): h = 3*h + 1  # h = 1,4,13,40,121.....
    while(h >= 1):
        for i in range(h,N):
            for j in range(i,h-1,-h):
                compare_num += 1
                if data[j] < data[j-h]:
                    sort.exch(data, j, j-h)
                    exch_num += 1
                    #print data
                else: 
                    break 
        h /= 3
            
    return compare_num, exch_num                 

class Date():
    
    def __init__(self, year = 0, month = 0, day = 0):
        self.year = year
        self.month = month
        self.day = day
        
    def __lt__(self, date):
        if self.year < date.year:
            return True
        elif self.year > date.year:
            return False
        else:
            if self.month < date.month:
                return True
            elif self.month > date.month:
                return False
            else:
                if self.day < date.day:
                    return True
                else:
                    return False
    def __repr__(self):
        return (str(self.year) + ' - '+
                str(self.month) + ' - ' + 
                str(self.day))
        
if __name__ == '__main__':
    
    compare = [[],[],[],[]]  #记录 选择排序，插入排序，冒泡排序 和 希尔排序 的交换顺序
    exch = [[],[],[],[]]
    
    data = []   # 待排序的数组
    
    name = ['selectionSort','insertionSort','bubbleSort','shellSort'] # 标签名
    function = [selectionSort, insertionSort, bubbleSort, shellSort]  # 函数名
    max_num = 1000000
    min_num = 0  #待排序数组的取值范围 [max_num, min_num]
    
    number = 16  # 数组的长度： 2**number   这个参数根据情况修改

    # 生成指定长度的待排序数组
    for n in range(6,number):
        for j in range(2**n):
            data.append(random.randint(min_num, max_num))

        # 复制一份数组
        temp = data[:-1]
        # 计算每种算法所需要的交换次数和对比次数
        for i in range(4):
            compare_num, exch_num = function[i](data)
            compare[i].append(compare_num)
            exch[i].append(exch_num)
            data = temp[:-1]
    
    # 画出折线图
    marks = ['o','.','+','*']  
    x = list(range(6,number))
    plt.figure(num = 1)
    for compare_num, label_name, mark in zip(compare, name, marks):
        plt.plot(x, compare_num, label=label_name, marker = mark)
    plt.title('The relation between the length of list and compare time')
    plt.xlabel('The length of list: 2^n where: n = range(6,%d)' %number)
    plt.ylabel('Compare times')
    plt.legend()
    plt.show(1)
    
    
    plt.figure(2)
    for exch_num, label_num, mark in zip(exch, name, marks):
        plt.plot(x, exch_num, label = label_num, marker = mark)
    plt.title('The relation between the length of list and exchange time')
    plt.xlabel('The length of list: 2^n where: n = range(6,%d)' %number)
    plt.ylabel('Exchange times')
    plt.legend()
    plt.show(2)

    
    
