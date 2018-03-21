
'''
Created on 2018年3月21日

@author: wangs0622

剑指offer第12题：矩阵中的路径

设计一个函数，用于判断一个矩阵中是否存在一条包含某个字符串所有字符的路径。路径从矩阵的任意
一格开始，每一步向矩阵的左、右、上、下移动一格，如果一条路径经过了矩阵的某一格，则该路径不
不能再进入该格
'''
import numpy as np


path_length = 0

def hasPath(matrix, string):
    '''
    input: 
    matrix: 指定的矩阵
    string: 指定的字符串
    
    output: True or False 代表是否存在路径 
    '''
    rows, cols = matrix.shape
    if rows < 0 or cols < 0 or len(string) < 0:
        return 0
    visted = np.zeros((rows, cols),dtype=bool)
    for i in range(rows):
        for j in range(cols):
            if(hasPathCore(matrix, rows, cols, i, j, string, visted)):
                return True
            
    return False

def hasPathCore(matrix, rows, cols, i, j, string, visited):
    global path_length 
    if path_length == len(string):
        return True
    
    has_path = False
    if 0<=i<rows and 0<=j<cols and matrix[i][j] == string[path_length] and not visited[i][j]:
        path_length += 1
        visited[i][j] = True
        has_path = hasPathCore(matrix, rows, cols, i-1, j, string, visited) or \
                hasPathCore(matrix, rows, cols, i+1, j, string, visited) or \
                hasPathCore(matrix, rows, cols, i, j-1, string, visited) or \
                hasPathCore(matrix, rows, cols, i, j+1, string, visited)
        if not has_path:
            path_length -= 1
            visited[i][j] = False
            
    return has_path

if __name__ == '__main__':
    A = np.array(
        [['a','b','t','g'],
        ['c','f','c','s'],
        ['j','d','e','h'],
        ['k','s','m','z']]
        )
    string = 'zmedfctg'
    print(hasPath(A, string))
    
        
        
    
            
