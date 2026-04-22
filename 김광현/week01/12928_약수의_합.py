# 문제: 약수의 합
# URL: https://school.programmers.co.kr/learn/courses/30/lessons/12928

def solution(n):
    divisors = []
    for i in range(n):
        if n % (i + 1) == 0:
            divisors.append(i + 1)
    answer = sum(divisors)
    return answer