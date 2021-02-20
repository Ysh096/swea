import sys
sys.stdin = open("input.txt", "r")

#가장 긴 회문의 길이를 찾는 함수
def solution(row):
    # (홀수일 때)양옆이 같은지 확인하는 방법으로 만들어보자
    p_length_max_odd = 0
    for idx in range(1, 99): #양옆은 제외해도 무방
        i = 1
        while idx-i>=0 and idx+i<=99:
            if row[idx-i] == row[idx+i]:
                i += 1
            else:
                i -= 1
                break #중간에 회문이 끝난 경우
        else:
            i -= 1 #끝까지 가서 회문이 끝난 경우
        #i는 idx를 중심으로 하는 회문의 길이를 계산할 때 사용함
        #회문의 길이
        p_length_odd = 1 + 2*i
        if p_length_max_odd < p_length_odd:
            p_length_max_odd = p_length_odd
    #짝수일 때
    p_length_max_even = 0
    for idx in range(99):
    #다음 문자와 지금 문자가 같은지 확인, 같다면 그 다음도 같은지 확인
        if row[idx] == row[idx+1]:
            i = 1
            while idx-i>=0 and idx+1+i<=99:
                if row[idx-i] == row[idx+1+i]:
                    i += 1
                else:
                    i -= 1
                    break
            else:
                i -= 1
            p_length_even = 2 + 2*i
            if p_length_max_even < p_length_even:
                p_length_max_even = p_length_even
    #p_length_max_even, p_length_max_odd에 각 행의 홀, 짝 최대 회문 길이가 주어짐
    if p_length_max_even > p_length_max_odd:
        return p_length_max_even
    else:
        return p_length_max_odd

def transpose(pan):
    pan_trans = [[0]*100 for _ in range(100)]
    for i in range(100):
        for j in range(100):
            pan_trans[j][i] = pan[i][j]
    return pan_trans
#100*100 글자판
for _ in range(10):
    tc = int(input())
    pan = [input() for _ in range(100)]
    pan_trans = transpose(pan) #전치행렬
    result = []
    for i in range(100):
        #각 행의 회문 최대 길이
        result += [solution(pan[i])]
        result += [solution(pan_trans[i])]

    print('#{} {}'.format(tc, max(result)))


###교수님 풀이###
def my_find2(M):
    for i in range(N):
        for j in range(N-M+1):
            tmp = words[i][j:j+M]
            tmp2 = zwords[i][j:j+M]

            if tmp == tmp[::-1] or tmp2 == tmp2[::-1]:
                return M
    return 0


def my_find(M):
    #전체크기가 N이다.
    for i in range(N):
        #부분 문자열의 시작점
        for j in range(N-M+1):
            #스왑을 응용한 회문검사

            #가로 검사
            for k in range(M//2):
                #앞뒤검사
                if words[i][j+k] != words[i][j+M-1-k]:
                    break
                #회문이다.
                elif k == M//2 - 1:
                    return M
            #세로 검사
            for k in range(M//2):
                if words[j+k][i] != words[j+M-1-k][i]:
                    break
                elif k == M//2 - 1:
                    return M
    return 0

for tc in range(10):
    tc_num = int(input())

    N = 100

    words = [input() for i in range(N)]
    zwords = list(zip(*words)) #안썼으면 하는 방법

    #가장 길이가 긴 회문검사를 한다.

    for i in range(N, 0, -1):
        ans = my_find(i)
        #ans = my_find2(i)
        if ans != 0:
            break

    print("#{} {}".format(tc_num, ans))



