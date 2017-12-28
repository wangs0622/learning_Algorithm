#_*_ encoding: utf-8 _*_
'''
Created on 2017年12月28日

@author: wangs0622

function: 有序符号表
'''
   
class OrderedST():
    
    def __init__(self):
        self.keys = [] 
        self.values = []
    
    def put(self, key, value):
        '''
        function: 将 key=value 这一键值对按顺序插入
        '''
        
        if value is None:
            raise ValueError('value can not be None')
        if key is None:
            raise KeyError('key can not be None')
        
        if self.len() == 0: 
            self.keys.append(key)
            self.values.append(value)
            return 
            
        i = self.rank(key)
        if i >= self.len():  #如果 key 最大，直接插入
            self.keys.append(key)
            self.values.append(value)
            return 
        
        if self.keys[i] == key:
            self.values[i] = value
    
        else:
            self.keys.insert(i, key)
            self.values.insert(i, value)
    
    def get(self, key):
        if key in self.keys:
            return self.values[self.keys.index(key)]
        else:
            return None
    
    def len(self):
        return self.size()
    
    def size(self, lokey=None, hikey=None):
        if lokey == hikey == None:
            return len(self.keys)
        elif lokey != None and hikey == None:
            return len(self.keys[self.rank(lokey):])
        elif lokey == None and hikey != None:
            return len(self.keys[:self.rank(hikey)])
        else:
            return len(self.keys[self.rank(lokey):self.rank(hikey)])
        
    def rank(self, key):
        '''
        function: 二分查找确定 key 的位置
        '''
        lo = 0
        hi = self.len()-1
        while lo <= hi:
            mid = lo + int((hi-lo)/2)
            if key < self.keys[mid]:
                hi = mid - 1
            elif key > self.keys[mid]:
                lo = mid + 1
            else:
                return mid
        return lo
    
    def delete(self, key):
        if key in self.keys:
            value = self.values.pop(self.keys.index(key))
            self.keys.remove(key)
            return (key, value)
        else:
            raise KeyError('key:"{}" is not found'.format(key))
    
    def contians(self, key):
        if key in self.keys:
            return True
        else: 
            return False
        
    def min(self):
        return self.keys[0]
    
    def max(self):
        return self.keys[-1]
    
    def floor(self, key):
        if key in self.keys:
            return key
        i = self.rank(key)
        if i-1 < 0:
            raise KeyError('there is not key in keys list samller than the given key')
        return self.keys[i-1]
        
    def ceiling(self, key):
        if key in self.keys:
            return key
        i = self.rank(key)
        if i >= self.len()-1:
            raise KeyError('there is not key in keys list bigger than the given key')
        return self.keys[i]
    
    def select(self, k):
        return self.keys[k]
    
    def deleteMin(self):
        return self.delete(self.min())
        
    def deleteMax(self):
        return self.delete(self.max())
    
    def getKeys(self, lokey=None, hikey=None):
        '''
        function: 返回大于等于 lokey 且 小于 hikey 的所有 key 值， lokey 与 hikey可以不必在 self.keys 中
        '''
        if lokey == hikey == None:
            return self.keys
        elif lokey is not None and hikey is None:
            return self.keys[self.rank(lokey):]
        elif lokey is None and hikey is not None:
            return self.keys[:self.rank(hikey)]
        else:
            return self.keys[self.rank(lokey):self.rank(hikey)]
        


if __name__ == '__main__':
    st = OrderedST()
    st.put('b','b')
    st.put('y','g')
    st.put('s','d')
    st.put('f','b')
    st.put('m','1d')
    print(3 == st.rank(st.select(3)))
    print('f' == st.select(st.rank('f')))