# _*_ encoding:utf-8 _*_
'''
Created on 2017/11/29

@author: wangs0622

 定义 Queue 类, 属于先进先出队列，API 如下：
——————————————————————————————————————————————————
    __init__()       初始化一个空的 Quene
    isEmpty()        判断是否为空
    enqueue(data)    从尾部添加一个元素
    dequeue()        从头部删除一个元素并返回
    size()           返回队列中的元素个数
——————————————————————————————————————————————————
'''

from .Node import Node
class Queue():
    
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0
        
    def isEmpty(self):
        return self.length == 0
    
    def enqueue(self, data):
        if self.isEmpty():
            self.first = self.last = Node(data = data)
        else:
            old_last = self.last
            self.last = Node(data = data)
            old_last.next = self.last
        self.length += 1
        
    def dequeue(self):
        if self.isEmpty():
            raise QueueEmptyError()
        else:
            data = self.first.data
            if self.length == 1:
                self.first = self.last = None
            else:
                self.first = self.first.next
            self.length -= 1
            return data
        
    def __iter__(self):
        temp = self.first
        while True:
            if temp is None:
                break
            else:
                yield temp
                temp = temp.next
                
    def __repr__(self):
        s = ''
        for node in self:
            s = s + str(node.data) + ' <- '
        return s[:-4]
                
class QueueEmptyError():
    pass

def testDequeue(queue):
    try:
        data = queue.dequeue()
    except:
        return "this queue is empty"
    return data
    
    
if __name__ == '__main__':
    queue = Queue()
    print( "queue: ", queue)
    
    queue.enqueue(1)
    print( "queue: ", queue)
    
    queue.enqueue(2)
    print( "queue: ", queue)
    
    queue.enqueue(3)
    print( "queue: ", queue)
    
    queue.enqueue(4)
    print( "queue: ", queue)
    
    queue.enqueue(5)
    print( "queue: ", queue)
    
    queue.enqueue(6)
    print( "queue: ", queue)
    
    print( testDequeue(queue))
    print( "queue: ", queue)
    
    print( testDequeue(queue))
    print( "queue: ", queue)
    
    print( testDequeue(queue))
    print( "queue: ", queue)
    
    print( testDequeue(queue))
    print( "queue: ", queue)
    
    print( testDequeue(queue))
    print( "queue: ", queue)
    
    print( testDequeue(queue))
    print( "queue: ", queue)
    
    print( testDequeue(queue))
    print( "queue: ", queue)
    
    print( testDequeue(queue))
    print( "queue: ", queue)
