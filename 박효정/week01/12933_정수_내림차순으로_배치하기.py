def solution(n):
    lst = list(str(n))

    for i in range(len(lst)):
        for j in range(i):
            if int(lst[j]) < int(lst[i]):
                lst[j], lst[i] = lst[i], lst[j]
    ans = ''
    for s in lst:
        ans += s

    answer = int(ans)
    return answer

'''
    def solution(n):
        ls = list(str(n))
        ls.sort(reverse = True)
        return int("".join(ls))
'''