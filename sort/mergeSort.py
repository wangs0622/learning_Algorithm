# _*_ encoding: utf-8 _*_

'''
Created on 2017/12/1

@author: wangs0622
'''
import sort
from time import time
from random import randint
from primarySort import shellSort, insertionSort
import matplotlib.pyplot as plt
        
def merge(data, lo, mid, hi):
    
    left = lo
    right = mid
    
    temp = data[:]
    for i in range(lo, hi):
        
        if left >= mid:
            data[i] = temp[right]
            right += 1
        elif right >= hi:
            data[i] = temp[left]
            left += 1
        elif temp[left] < temp[right]:
            data[i] = temp[left]
            left += 1
        else:
            data[i] = temp[right]
            right += 1

def mergeSort(data, lo = None, hi = None):
    if lo == None: lo = 0
    if hi == None: hi = len(data)
    if lo >= hi:
        raise HiSmallerThanLo
    
    if hi <= lo + 1: return ''
    mid = lo + (hi - lo)/2
    mergeSort(data, lo, mid)
    mergeSort(data, mid, hi)
    merge(data, lo, mid, hi)
    
def mergeSortBU(data, lo = None, hi = None):
    if lo == None: lo = 0
    if hi == None: hi = len(data)
    
    if lo >= hi:
        raise HiSmallerThanLo
    N = hi - lo
    sz = 1
    while sz < N:
        for low in range(lo, N-sz, 2*sz):
            merge(data, low, low+sz, min(low+2*sz, hi))
        sz *= 2
        
def mergeSortWithPrimary(data, lo = None, hi = None):
    if lo == None: lo = 0
    if hi == None: hi = len(data)
    if lo >= hi:
        raise HiSmallerThanLo
    
    if hi <= lo + 10:
        insertionSort(data, lo, hi)
        return ''

    mid = lo + (hi - lo)/2
    mergeSort(data, lo, mid)
    mergeSort(data, mid, hi)
    merge(data, lo, mid, hi)
    
def mergeSortWithPrimaryAndJudge(data, lo = None, hi = None):
    if lo == None: lo = 0
    if hi == None: hi = len(data)
    if lo >= hi:
        raise HiSmallerThanLo
    
    if hi <= lo + 10:
        insertionSort(data, lo, hi)
        return ''

    mid = lo + (hi - lo)/2
    mergeSort(data, lo, mid)
    mergeSort(data, mid, hi)
    if data[mid-1] > data[mid]:
        merge(data, lo, mid, hi)
    
class NotSortedError(Exception):
    pass

class HiSmallerThanLo(Exception):
    pass



def main_mergeSort_VS_shellSort():
    data = []
    use_times = [[],[]]
    max_num = 1000000
    min_num = 0
    number = 16  # 数组的长度的最大值    2 的 number 次方
    for n in range(6,number):
        for j in range(2**n):
            data.append(randint(min_num, max_num))
        
        temp = data[:]
        
        t1 = time()
        shellSort(data)
        t2 = time()
        if sort.isSorted(data):
            use_times[0].append(t2-t1)
        else:
            raise NotSortedError()
        
        data = temp
        
        t3 = time()
        mergeSort(data, 0, len(data))
        t4 = time()
        if sort.isSorted(data):
            use_times[1].append(t4-t3)
        else:
            raise NotSortedError()
    
    name = ['shellSort','mergeSort']
    marks = ['o','+']  
    x = list(range(6,number))
    plt.figure(num = 1)
    for use_time, label_name, mark in zip(use_times, name, marks):
        plt.plot(x, use_time, label=label_name, marker = mark)
    plt.title('shellSort  -- VS --  mergeSort')
    plt.xlabel('The length of list: 2^n where: n = range(6,%d)' %number)
    plt.ylabel('use time(s)')
    plt.legend()
    plt.show(1)  
    
    
def main_mergetSort_VS_ImproveMergeSort():
    data = []
    use_times = [[],[],[]] # 对应与并归排序，改进方法1，改进方法1+2
    max_num = 1000000
    min_num = 0
    min_number = 6
    number = 12  # 数组的长度的最大值    2 的 number 次方
    for n in range(min_number,number):
        for j in range(2**n):
            data.append(randint(min_num, max_num))
        temp = data[:]
        
        t1 = time()
        mergeSort(data)
        t2 = time()
        if sort.isSorted(data):
            use_times[0].append(t2-t1)
        else:
            raise NotSortedError()
        
        data = temp[:]
        
        t3 = time()
        mergeSortWithPrimary(data)
        t4 = time()
        if sort.isSorted(data):
            use_times[1].append(t4-t3)
        else:
            raise NotSortedError()
        
        data = temp[:]
        
        t5 = time()
        mergeSortWithPrimaryAndJudge(data)
        t6 = time()
        if sort.isSorted(data):
            use_times[2].append(t6-t5)
        else:
            raise NotSortedError()
        
    name = ['mergeSort', 'improveMergeSort1', 'improveMergeSort1+2']
    marks = ['o','+','*']  
    x = list(range(min_number,number))
    plt.figure(num = 1)
    for use_time, label_name, mark in zip(use_times, name, marks):

        plt.plot(x, use_time, label=label_name, marker = mark, alpha=0.5)
    plt.title('MergeSort  -- VS --  improvemergeSort')
    plt.xlabel('The length of list: 2^n where: n = range(6,%d)' %number)
    plt.ylabel('use time(s)')
    plt.legend()  
    plt.show(1)

if __name__ == '__main__':
    #main_mergeSort_VS_shellSort()
    main_mergetSort_VS_ImproveMergeSort() 
        
        