'''
Created on 2018年3月24日

@author: wangs0622

'''

def power(base, exponent):
    if base == 0 and exponent < 0:
        raise ValueError("exponent must be not negative when base equals 0")
    if not isinstance(exponent, int):
        raise ValueError("exponent must be int")
    
    abs_exponent = exponent if exponent > 0 else -exponent
    
    result = powerCore(base, abs_exponent)
    if exponent < 0:
        result = 1.0/result
    return result
    
    
def powerCore(base, abs_exponent):
    if abs_exponent == 0:
        return 1
    if abs_exponent == 1:
        return base
    
    result = power(base, abs_exponent >> 1)
    result *= result
    if abs_exponent & 1:
        result *= base
    return result

if __name__ == '__main__':
    print(power(2.1,-3.1))
        
