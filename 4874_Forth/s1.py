import sys
sys.stdin = open('input.txt', 'r')

def Forth(L):
    stack = []
    for i in range(len(L)):
        try:
            z = int(L[i])
            stack.append(z) # 숫자는 stack에 넣기
        except: # 숫자가 아닌 경우
            if L[i] == '.': # 끝난 경우
                break
            else:
                # 사칙연산 기호인 경우
                if len(stack) >= 2:
                    A = stack.pop()
                    B = stack.pop()
                else:
                    return ['error']
                if L[i] == '+':
                    stack.append(A + B)
                elif L[i] == '-':
                    stack.append(A - B)
                elif L[i] == '*':
                    stack.append(A * B)
                else:
                    stack.append(A // B)
    if len(stack) == 1:
        return stack
    else:
        return ['error']
T = int(input())
for tc in range(1, T+1):
    L = input().split()
    print('#{} {}'.format(tc, *Forth(L)))


