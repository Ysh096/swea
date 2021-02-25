import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    N, password = input().split()
    stack = []
    for i in password:
        if len(stack) == 0:
            stack.append(i)
        else:
            if stack[-1] == i:
                stack.pop()
            else:
                stack.append(i)
    print('#{} {}'.format(tc, ''.join(stack)))