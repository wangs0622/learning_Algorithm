# _*_ encoding: utf-8 _*_
'''
Created on 2017/11/29

@author: wangs0622

Bag: 背包是一种不支持从删除元素的集合类型，它的目的就是帮助人们收集，并迭代遍历
所有的元素，也可以检查背包是否为空或者检查背包元素的个数。

API
————————————————————————————————————————————————
class Bag()
————————————————————————————————————————————————
__init__(self)              创建一个空的背包
add(self, data)             添加一个元素
isEmpty()                   检查是否为空
size()                      返回背包元素个数
————————————————————————————————————————————————

其实就相当于一个不使用  pop 方法的堆栈 
'''

from .Stack import Stack

class Bag(Stack):
    
    def __init__(self):
        Stack.__init__(self)
        
    def add(self, data):
        self.push(data)
        
if __name__ == '__main__':
    bag = Bag()
    bag.add(1)
    bag.add(2)
    print( bag)
    print( bag.isEmpty())
