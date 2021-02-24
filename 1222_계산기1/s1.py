import sys
sys.stdin = open('input.txt', 'r')
#+와 숫자만 주어지는 후위계산!
#숫자는 출력, +는 스택의 top과 우선순위를 따져서
#우선순위가 더 크면 앞의 것을 pop으로 출력하고 뒤의 것은 push!
#+만 있으므로 +를 마주칠때마다 pop 후에 stack에 push
for tc in range(1, 11):
    Len = int(input()) #문자열 계산식의 길이
    string = input()
    stack = []
    result = ''
    for val in string:
        if val == '+':
            if len(stack) > 0:
                if stack[-1] == '+':
                    result += stack.pop()
                    stack.append(val)
            else:
                stack.append(val)
        else: #숫자인 경우
            result += val
    #for문이 끝나면 stack에 하나가 남아있게 된다.
    result += stack.pop()
    # print(result)
    calc = [] #계산을 위한 스택
    for val in result:
        if ord('0') <= ord(val) <= ord('9'):
            calc.append(int(val))
        elif val == '+': #'+'를 만나면
            B = calc.pop()
            A = calc.pop()
            calc.append(A + B)
    print('#{} {}'.format(tc, calc[-1]))




