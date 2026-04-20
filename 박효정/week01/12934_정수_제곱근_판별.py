import math

def solution(n):
    n2 = math.sqrt(n)
    if int(n2) == n2:
        return (n2+1)**2
    else:
        return -1
'''
def nextSqure(n):
    sqrt = n ** (1/2) 

    if sqrt % 1 == 0:
        return (sqrt + 1) ** 2
    return 'no'
'''
