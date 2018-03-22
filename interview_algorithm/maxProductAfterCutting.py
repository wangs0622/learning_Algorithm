'''
Created on 2018年3月22日

@author: wangs0622

剑指  offer 14 剪绳子问题
给一根长度为 n 的绳子，请把绳子切成 m 段，m, n 都为整数，且 m > 1, n >1,问切成好的绳子
的长度乘积最大等于多少？

从 m > 1 可知，绳子必须切。 如果绳子的长度为 1，必须切的时候，一段为 0 一段为 1，所以当 n = 1 
的时候，返回值应该等于 0
对于 n = 2, 以及 n = 3 的情况，切完后的乘积的最大值没有原值大，所以需要单独返回。
'''

def maxProductAfterCutting_DP(n):
    if n < 0: 
        raise ValueError('n must be positive')
    if not isinstance(n, int):
        raise ValueError('n must be int')
    if n < 2: return 0
    if n == 2: return 1
    if n == 3: return 2
    # 之所以 n == 3 以前的单独返回，是因为其值小于 n
    product = [0,1,2,3]
    for i in range(4, n+1):
        max_product = 0
        for j in range(1, i//2+1):
            max_product = max(max_product, product[j]*product[i-j])
        product.append(max_product)
    return product[n]

def maxProductAfterCutting_Greedy(n):
    if n < 0: 
        raise ValueError('n must be positive')
    if not isinstance(n, int):
        raise ValueError('n must be int')
    if n < 2: return 0
    if n == 2: return 1
    if n == 3: return 2
    number_length_3 = n // 3
    number_length_after = n % 3  # 尽量切成 3 后，剩下的长度
    if number_length_after == 1:
        number_length_3 -= 1  # 为了让最后的长度等于 4
    number_length_after_2 = (n - number_length_3 * 3) // 2  # 切完 3 最后的长度，切成 2
    
    return (3**number_length_3) * (2**number_length_after_2)  

if __name__ =='__main__':
    n = 100
    print(maxProductAfterCutting_DP(n))
    print(maxProductAfterCutting_Greedy(n))
            
    
    