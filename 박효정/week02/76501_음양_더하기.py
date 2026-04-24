# 문제: 음양 더하기
# URL: https://school.programmers.co.kr/learn/courses/30/lessons/76501

def solution(absolutes, signs):
    ans = 0
    for i in range(len(absolutes)):
        if signs[i]:
            ans += absolutes[i]
        else:
            ans -= absolutes[i]

    return ans


'''
def solution(absolutes, signs):
    answer=0
    for absolute,sign in zip(absolutes,signs):
        if sign:
            answer+=absolute
        else:
            answer-=absolute
    return answer
'''
