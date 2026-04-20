def solution(x):
    st = str(x)
    n = 0
    for s in st:
        n += int(s)

    if x % n == 0:
        return True
    else:
        return False