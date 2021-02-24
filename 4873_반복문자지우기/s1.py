import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    strings = input()
    stack = []
    for string in strings:
        if len(stack) == 0:
            stack.append(string) #스트링이 비어있으면 하나 추가
        elif string == stack[-1]: #직전 값과 같으면
            stack.pop() #직전 값 제거하고
            continue #다음 문자 확인
        else:
            stack.append(string) #직전 값과 다르면 추가
    print('#{} {}'.format(tc, len(stack)))