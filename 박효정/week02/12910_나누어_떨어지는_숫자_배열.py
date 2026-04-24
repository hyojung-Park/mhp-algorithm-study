# 문제: 나누어 떨어지는 숫자 배열
# URL: https://school.programmers.co.kr/learn/courses/30/lessons/12910

def solution(arr, divisor):
    ans = [n for n in arr if not n % divisor]
    ans.sort()

    if not ans:
        return [-1]

    return ans