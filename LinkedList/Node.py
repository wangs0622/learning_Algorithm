# _*_ encoding: utf-8 _*_


class Node():
     
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next
        
    def __repr__(self):
        return 'data: ' + str(self.data)
