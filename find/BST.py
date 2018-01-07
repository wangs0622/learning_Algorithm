# _*_ encoding: utf-8 _*_
'''
Created on 2018/1/3

@author: wangs0622
'''

class Node():
    '''
    This Node class defines a node object, which contains two child-node,one is 
    left-childnode and another is right-childnode. 
    
    Every node also contains a key item that is camparable, and a value item, 
    this represents the value corresponding to the key.
    
    Beside, a node object contians a variable: N, representing the number node
    in it's child-node, inculding left, right child-node and itself.
    '''
    def __init__(self, key=None, value=None, lchild=None, rchild=None, N=1):
        self.key = key
        self.value = value
        self.lchild = lchild
        self.rchild = rchild
        self.N = N
        
    def __repr__(self):
        return " key: {0} \n value: {1} \n lchild:{2} \n rchild:{3} \n N:{4}".format(
            self.key, self.value, self.lchild, self.rchild, self.N
            )
        

def printBST(root):
    print('{{0}: {1}}'.format(root.key, root.value))
    if root.lchild != None:
        printBST(root.lchild)
    else:
        return
    
    if root.rchild != None:
        printBST(root.rchild)
    else:
        return
   

class BST():
    '''
    BST: Binary Search Tree
    '''


    def __init__(self, root=None):
        '''
        constructing a BST only with root node initially. 
        '''
        self.root = root
    
    def __len__(self):
        return self.root.N
    
    def __contains__(self, key):
        return self._bstSearch(self.root, key) is not None
    
    def _bstSearch(self, sub_tree, key):
        if sub_tree is None:
            return None
        elif sub_tree.key > key:
            return self._bstSearch(sub_tree.lchild, key)
            
        elif sub_tree.key < key:
            return self._bstSearch(sub_tree.rchild, key)
            
        else:
            return sub_tree
            
        
    def put(self, key, value, recursion=True):
        '''
        put the "key:value" into the BST. 
        if key is in BST, it will update it's value by the new value.
        else, it will create a new node and insert the new node in the BST.
        '''
        if value is None:
            raise ValueError('value can not be None')
        if key is None:
            raise KeyError('key can not be None')
        
        if self.root is None:
            self.root = Node(key, value)
            return
        if recursion:
            self._put(self.root, key, value)
        else:
            self._putWithOutRecursion(self.root, key, value)
        
    def _put(self, sub_tree, key, value):
        if sub_tree == None:
            return Node(key, value)
        
        if key == sub_tree.key:
            sub_tree.value = value
        elif key > sub_tree.key:
            sub_tree.rchild = self._put(sub_tree.rchild, key, value)
        else: 
            sub_tree.lchild = self._put(sub_tree.lchild, key, value)
        
        left_num = sub_tree.lchild.N if sub_tree.lchild is not None else 0
        right_num = sub_tree.rchild.N if sub_tree.rchild is not None else 0
        sub_tree.N = left_num + right_num + 1
        return sub_tree
    
    def _putWithOutRecursion(self, sub_tree, key, value):
        left_or_right = 0
        while sub_tree is not None:
            parents = sub_tree
            if sub_tree.key == key:
                sub_tree.value = value
                return
            elif sub_tree.key > key:
                sub_tree = sub_tree.lchild
                left_or_right = -1
            else:
                sub_tree = sub_tree.rchild
                left_or_right = 1
        if left_or_right == 1:
            parents.rchild = Node(key, value)
        else:
            parents.lchild = Node(key, value)
        self._plusN(key)
        
        
    def _plusN(self, key):
        sub_tree = self.root
        while sub_tree.key is not key:
            sub_tree.N += 1
            sub_tree = sub_tree.lchild if sub_tree.key > key else sub_tree.rchild        
    
    def get(self, key, recursion=True):
        
        if self.root == None: return
        if recursion:
            return self._get(self.root, key)
        else:
            return self._getWithOutRecursion(self.root, key)
    
    def _get(self, sub_tree, key):
        
        if sub_tree is None: return
        
        if sub_tree.key == key:
            return sub_tree.value
        elif sub_tree.key > key:
            return self._get(sub_tree.lchild, key)
        else:
            return self._get(sub_tree.rchild, key)

    def _getWithOutRecursion(self, sub_tree, key):

        while sub_tree is not None:
            if sub_tree.key == key:
                return sub_tree.value
            elif sub_tree.key > key:
                sub_tree = sub_tree.lchild
            else:
                sub_tree = sub_tree.rchild
        return None

    def size(self):
        return self._size(self.root)
    
    def _size(self, sub_tree):
        if sub_tree is None:
            return 0
        else:
            return sub_tree.N
        
        
        
        
if __name__ == '__main__':
    bst = BST()
    bst.put('g',1)
    bst.put('d',3)
    bst.put('z',2)
    bst.put('e',4)
    bst.put('y',4)
    bst.put('j',9)
    #print(bst.root)
    print(bst.get('y'))
    print(bst.get('r'))
    print('y' in bst)
    print(bst._bstSearch(bst.root, 'y').key)
    print(len(bst))

    '''
    print('----------------------------------')
    bst1 = BST()
    bst1.put('g',1,False)
    bst1.put('d',3,False)
    bst1.put('z',2,False)
    bst1.put('e',4,False)
    bst1.put('y',4,False)
    bst1.put('j',9,False)
    print(bst.get('y',False))
    print(bst.get('r',False))
    #print(bst1.root)
    '''
    
        
