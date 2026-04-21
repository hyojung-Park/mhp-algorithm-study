def solution(n):
    answer = ""
    s = str(n)
    arr = [i for i in s]
    arr.sort(reverse=-1)
    for i in arr: answer += i
    return int(answer)