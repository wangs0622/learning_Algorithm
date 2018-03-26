'''
Created on 2018年3月24日

@author: wangs0622

剑指 offer 20 题，表示数值的字符串

'''
i = 0
NUMBER_SET = {'0','1','2','3','4','5','6','7','8','9'}
def isNumber(string):
    global i
    if len(string) <= 0:
        return False
    number = scanInterger(string)
    #print('i ：', i)
    if i < len(string) and string[i] == '.':
        i += 1
        number = scanUnsignedInterger(string) or number
    if i < len(string) and string[i] in {'E','e'}:
        i += 1
        number = number and scanInterger(string)
        
        
    return number and i == len(string)
    
def scanInterger(string):
    global i
    if string[i] == '+' or string[i] == '-':
        i += 1
    return scanUnsignedInterger(string)

def scanUnsignedInterger(string):
    global i
    start = i
    while i < len(string) and string[i] in NUMBER_SET:
        i += 1
    return i > start

if __name__ == '__main__':
    string = '+123.23e832#'
    print(isNumber(string))
    
             
        
