# _*_ encoding: utf-8 _*_

'''
Created on 2017/11/29

@author: wangs0622
'''


def exch(datalist, i, j):
    '''
    - 交换位置
    '''
    datalist[i], datalist[j] = datalist[j], datalist[i]
    
def  less(data1, data2):
    '''
    - data1 < data2  则 return True
    - 在 Python 中，  __lt__ 重载了 < 。 所有只要我们的 data所需的类有此方法即可 
    '''
    return data1 < data2


def isSorted(data):
    '''
    - 检测 data 中的元素是否有序
    '''
    for i in range(len(data)-1):
        if data[i] > data[i+1]:
            return False
    return True
        
    
    
