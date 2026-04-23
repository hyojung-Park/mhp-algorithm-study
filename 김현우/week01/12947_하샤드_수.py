def solution(x):
    s = str(x)
    x_sum = 0
    for i in s: x_sum += int(i)
    if x%x_sum == 0:
        return True
    else: return False