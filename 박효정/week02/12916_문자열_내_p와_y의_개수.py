# 문제: 문자열 내 p와 y의 개수
# URL: https://school.programmers.co.kr/learn/courses/30/lessons/12916

def solution(s):
    p, y = 0, 0
    ans = True
    for i in s:
        if i == 'p' or i == 'P':
            p += 1
        elif i == 'y' or i == 'Y':
            y += 1

    if p != y:
        ans = False

    return ans