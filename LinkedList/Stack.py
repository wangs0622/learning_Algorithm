# _*_ encoding: utf-8 _*_

'''
Created on 2017年11月29日

@author: wangs0622

function: 使用链表的方式定义一个堆栈
'''

from .Node import Node

class StackEmptyError(Exception):
    '''
    stack is empty
    '''
    pass
        

class Stack():
    
    def __init__(self):
        self.first = None
        self.length = 0
        
    def isEmpty(self):
        return self.length == 0
    
    def push(self, data):
        old_first = self.first
        self.first = Node(data = data, next = old_first)
        self.length += 1
        
    def pop(self):
        if self.isEmpty():
            raise StackEmptyError()
        else:
            data = self.first.data
            self.first = self.first.next
            self.length -= 1
            return data
    
    def size(self):
        return self.length
    
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
            print( 'node:     ', node)
            s = s + str(node.data) + ' -> '
        return s[:-4]
    
    
def testPop(stack):
    try:
        data = stack.pop()
    except StackEmptyError:
        return "This stack is empty"
    return data
    
if __name__ == '__main__':
    stack = Stack()
    print( 'stack: ', stack)
    stack.push(1)
    print( 'stack: ', stack)
    stack.push(2)
    print( 'stack: ', stack)
    stack.push(3)
    print( 'stack: ', stack)
    stack.push(4)
    print( 'stack: ', stack)
    stack.push(5)
    print( 'stack: ', stack)
    stack.push(6)
    print( 'stack: ', stack)
    stack.push(7)
    print( 'stack: ', stack)
    stack.push(8)
    print( 'stack: ', stack)
    
    print( "pop: ", testPop(stack))
    print( 'stack: ', stack)
    
    print( "pop: ", testPop(stack))
    print( 'stack: ', stack)
    
    print( "pop: ", testPop(stack))
    print( 'stack: ', stack)
    
    print( "pop: ", testPop(stack))
    print( 'stack: ', stack)
    
    print( "pop: ", testPop(stack))
    print( 'stack: ', stack)
    
    print( "pop: ", testPop(stack))
    print( 'stack: ', stack)
    
    print( "pop: ", testPop(stack))
    print( 'stack: ', stack)
    
    print( "pop: ", testPop(stack))
    print( 'stack: ', stack)
    
    print( "pop: ", testPop(stack))
    print( 'stack: ', stack)
    
    
    print( "pop: ", testPop(stack))
    print( 'stack: ', stack)
    
    print( "pop: ", testPop(stack))
    print( 'stack: ', stack)
