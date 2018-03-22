
'''
Created on 2018年3月22日

@author: wangs0622

剑指 offer 13 题，机器人运动范围
问题： 在地面上有 m行  n 列的格子，机器人从坐标为（0,0） 的格子出发，每次只能上下左右的移动一格
，但不能进入行坐标与列坐标的位数之和大于 k 的格子，问，该机器人能到达多少个格子？
'''
import numpy as np

def robotMoveCounter(rows, cols, k):
    if rows <= 0 or cols <= 0 or k < 0:
        return 0
    visited = np.zeros((rows, cols), dtype=bool)
    
    counter = robotMoveCounterCore(visited, rows, cols, 0, 0, k)
    #point = np.where(visited == False)
    return counter

def robotMoveCounterCore(visited, rows, cols, row, col, k):
    counter = 0
    if 0 <= row < rows and 0 <= col < cols and not visited[row][col]:
        if check(row, col, k):
            visited[row][col] = True
            counter = 1 + robotMoveCounterCore(visited, rows, cols, row-1, col, k) + \
                            robotMoveCounterCore(visited, rows, cols, row+1, col, k) + \
                            robotMoveCounterCore(visited, rows, cols, row, col-1, k) + \
                            robotMoveCounterCore(visited, rows, cols, row, col+1, k)
    return counter        
                  
def check(row, col, k):
    if sum(numberToList(row))+sum(numberToList(col)) <= k:
        return True
    else:
        return False
    
def numberToList(number):
    temp_string = str(number)
    return [int(i) for i in temp_string]         

if __name__ == '__main__':
    rows = 30
    cols = 20
    k = 15 
    print(robotMoveCounter(rows, cols, k))