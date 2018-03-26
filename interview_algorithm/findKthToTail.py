'''
Created on 2018年3月26日

@author: wangs0622

剑指 offer 22 题，链表找那个导数第 k 个节点

'''

class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkList:
    def __init__(self):
        self.head = None

    def add(self, data):
        last_node = self.getLast()
        if last_node is None:
            self.head = ListNode(data)
            return
        new_node = ListNode(data)
        last_node.next = new_node
        del last_node
        
    def getLast(self):
        cur_node = self.head
        if cur_node is None:
            return None
        while cur_node.next is not None:
            cur_node = cur_node.next
        return cur_node

length_list_less_k = False

def findKthToTail(linklist, k):
    global length_list_less_k
    if linklist.head is None or k == 0:
        return None
    before = linklist.head
    behind = linklist.head
    i = 1
    while i < k:
        if before.next is not None:
            before = before.next
        else:
            length_list_less_k = True
            return None
        i += 1
    while before.next is not None:
        before = before.next
        behind = behind.next
    return behind
        
    
    
if __name__ == "__main__":
    
    a = [1,2]
    test_link_list = LinkList()
    for i in a:
        test_link_list.add(i)
    
    temp = test_link_list.head
#    while temp is not None:
#        print(temp.data)
#        temp = temp.next
    
    k = 4
    result = findKthToTail(test_link_list, k)
    if result is None:
        if length_list_less_k:
            print("链表长度小于 k, k={0}".format(k))
        print(result)
    else:
        print("倒数第 {0} 个节点元素为： {1}".format(k, result.data))
            
        
        
        
    
    


    
        
