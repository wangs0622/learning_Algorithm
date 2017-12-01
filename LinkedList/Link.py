# _*_ encoding:utf-8 _*_

'''
Created on 2017/11/28

@author: wangs0622
version: python2.7
'''


from LinkedList import Node
    
# 定义链表类，link

class Link():
    
    def __init__(self):
        self.first = None
        self.length = 0
        
    def isEmpty(self):
        '''
        judge this is empty or not
        '''
        return self.length == 0
    
    def appendFirst(self, node):
        '''
        add a node at the first of the link
        '''
        if self.isEmpty():
            self.first = node
            self.length = 1
        else:
            old_first = self.first
            self.first = node
            self.first.next = old_first
            self.length += 1
    
    def dealFirst(self):
        '''
        deal the first node of the link
        '''
        if self.isEmpty():
            print "This link is empty"
        else:
            self.first = self.first.next
            self.length -= 1
        
    def size(self):
        '''
        get the length of the link
        '''
        return self.length
    
    def __iter__(self):
        temp = self.first
        while True:
            if temp.next == None:
                break
            else:
                yield temp 
                temp = temp.next
        
    def __repr__(self):
        '''
        print this link
        '''
        if self.isEmpty(): 
            return ""
        else:
            s = ''
            for node in self:
                s = s + str(node.data) + ' -> '
            return s[:-4]
                                      
if __name__ == '__main__':
 
    link = Link()
    link.appendFirst(Node(data = 'first'))
    link.appendFirst(Node(data = 'second'))
    link.appendFirst(Node(data = 'third'))
    link.appendFirst(Node(data = 'fourth'))
    link.appendFirst(Node(data = 'fifth'))
    link.appendFirst(Node(data = 'sixth'))
    
    print "link: ", link
    print "link length: ", link.length
    
    
    link.dealFirst()

    print "link: ", link
    print "link length: ", link.length

    
    link.dealFirst()

    print "link: ", link
    print "link length: ", link.length
    
    link.dealFirst()

    print "link: ", link
    print "link length: ", link.length
    
    link.dealFirst()

    print "link: ", link
    print "link length: ", link.length
    
    link.dealFirst()
    print "link: ", link
    print "link length: ", link.length
    
    link.dealFirst()
    print "link: ", link
    print "link length: ", link.length

    link.dealFirst()
    print "link: ", link
    print "link length: ", link.length
    
    link.dealFirst()
    print "link: ", link
    print "link length: ", link.length
    
    link.dealFirst()
    print "link: ", link
    print "link length: ", link.length
    
    