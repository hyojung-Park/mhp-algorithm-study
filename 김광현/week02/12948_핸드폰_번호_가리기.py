# 문제: 핸드폰 번호 가리기
# URL: https://school.programmers.co.kr/learn/courses/30/lessons/12948

def solution(phone_number):
    answer = ""
    last_num = len(phone_number) - 4
    print(last_num)
    for i in range(last_num):
        answer += "*"
    for i in range(4):
        answer += phone_number[i -4]
    return answer