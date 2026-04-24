# 문제: 가운데 글자 가져오기
# URL: https://school.programmers.co.kr/learn/courses/30/lessons/12903

def solution(s):
    l = len(s)
    if l % 2 != 0:
        return s[l//2]
    else:
        return s[l//2-1: l//2+1]