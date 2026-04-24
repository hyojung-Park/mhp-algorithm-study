# 문제: 핸드폰 번호 가리기
# URL: https://school.programmers.co.kr/learn/courses/30/lessons/12948

def solution(phone_number):
    idx = len(phone_number) - 4
    return '*' * idx + phone_number[idx:]