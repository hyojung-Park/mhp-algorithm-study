def solution(n):
    answer = 0
    str1 = str(n)
    for s in str1:
        answer += int(s)

    return answer