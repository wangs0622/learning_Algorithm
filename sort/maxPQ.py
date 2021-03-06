# _*_ encoding: utf-8 _*_
'''
Created on 2017\12\22

@author: wangs0622

version: python3.6.4
'''
from collections import deque
import math
import matplotlib.pyplot as plt

class MaxPQ():
    '''
    FUNCTION: 基于 deque 实现优先队列
    '''
    def __init__(self, iterable=None, maxsize=0):
        self.maxsize = maxsize
        self.queue = deque(iterable, maxsize)
        
    def insert(self, item):
        '''
        function: 向优先队列中插入一个新的元素
        '''
        self.queue.append(item)
    
    def dealMax(self):
        '''
        function: 删除最大的元素并返回
        '''
        temp = self.max()
        self.queue.remove(temp)
        return temp
    
    def max(self):
        '''
        function: 返回最大值
        '''
        max_value = self._queue[0]
        for x in self.queue:
            max_value = max(x, max_value)
        return max_value
        
        
        
    def size(self):
        return len(self.queue)
    
    def isEmpty(self):
        return self.size() == 0
    

def printHeap(heap, startpos=0):
    size = len(heap) - 1  # 需要画出的节点的个数
    lines = int(math.floor(math.log(size, 2)))  # 总共有多少行，从零开始
    print(lines)
    lastlength = 2**lines     #最底层有多少个节点
    y = lines + 1
    x = 0
    space = lastlength/2
    i = 0

    if startpos == 1:
        temp = 0
    else:
        temp = 1

    
    for index in range(startpos,len(heap)):
        item = heap[index]
        if index + temp == 2**i:
            x = space
            y -= 1
            plt.plot(x,y,'ro')
            plt.text(x,y+0.1,item) 
            i += 1 
            space /= 2  
        else:
            x += 4*space
            plt.plot(x,y,'ro')
            plt.text(x,y+0.1,item)
    
    plt.show()
         
        
        
        

def swim(heap, k):
    '''
    function: 二叉堆的上浮操作
    
    print(k)
    print(type(k))
    print(math.floor(k/2))
    print(type(math.floor(k/2)))
    '''
    while k > 1 and heap[math.floor(k/2)] < heap[k]:
        heap[math.floor(k/2)], heap[k] = heap[k], heap[math.floor(k/2)]
        k = math.floor(k/2)
        
        
def sink(heap, k):
    '''
    function: 二叉堆的上浮操作
    '''
    while 2*k <= len(heap):
        j = 2*k
        if j+1 <= len(heap):
            if heap[j+1] > heap[j]:
                j += 1
        if heap[k] > heap[j]: break
        heap[k], heap[j] = heap[j], heap[k]
        k = j
               
class MaxPQbasedHeap(MaxPQ):
    
    def __init__(self, maxsize=None):
        self.queue = deque([0], maxsize)
        
    def insert(self, item):
        self.queue.append(item)
        swim(self.queue, len(self.queue)-1)
        
    def dealMax(self):
        max_value = self._queue[1]
        self.queue[1], self.queue[-1] = self.queue[-1], self.queue[1]
        sink(self.queue, 1)
        
if __name__ == '__main__':
    
    pq = MaxPQbasedHeap()
    print(pq.queue)
    items = 'qwertyuiopasdfghjklzxcvbnm'
    for x in items:
        pq.insert(x)
    print(pq.queue)
    printHeap(pq.queue,1)
    
    
    
