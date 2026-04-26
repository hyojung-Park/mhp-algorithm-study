# 문제: 가운데 글자 가져오기
# URL: https://school.programmers.co.kr/learn/courses/30/lessons/12903

def solution(s):
    answer = ''
    if len(s) % 2 == 0:
        return s[len(s)//2 - 1] + s[len(s)//2]
    else:
        return s[len(s)//2]
