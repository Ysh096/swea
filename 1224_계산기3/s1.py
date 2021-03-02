import sys
sys.stdin = open('input.txt')
#괄호 '('는 무조건 넣어주고, 스택 안에서 '('가 앞에 있으면 신경쓰지 않는다.
#괄호 ')'를 만나면 '('를 만날 때 까지 pop해서 출력하고, '('은 버린다.
#+-끼리 만나면 앞의 것을 pop해서 출력하고 뒤의 것은 스택에 쌓는다.
#*/끼리 만나면 앞의 것을 pop해서 출력하고 뒤의 것은 스택에 쌓는다.
for tc in range(1, 11):
    Len = int(input())
    string = input()
    op = {'(': 0, '+': 1, '*': 2}
    stack = []
    result = ''
    for v in string:
        if v == '(':
            stack.append('(')
        elif v == ')':
            while True:
                a = stack.pop()
                if a != '(':
                    result += a
                else:
                    break
                # a = '('면 아무것도 하지 않음으로써 pop만 하여 버리는 동작이 됨
        elif v in op: # 연산자인 경우
            while stack:
                if op[stack[-1]] < op[v]: # * 앞에 +가 있는 경우
                    stack.append(v)
                    break
                elif op[stack[-1]] > op[v]: # +앞에 *가 있는 경우
                    result += stack.pop()
                else:
                    result += stack.pop() # +가 +를, 혹은 *가 *를 만난 경우
                    stack.append(v)
                    break
        else: # 숫자인 경우
            result += v
    #2. 계산하기
    #숫자면 스택에 쌓기
    #연산자면 스택에서 피연산자 두개를 꺼내서 계산한 후 스택에 넣기
    calc = []
    for val in result:
        if ord('0') <= ord(val) <= ord('9'):
            calc.append(int(val))
        else:
            B = calc.pop()
            A = calc.pop()
            if val == '+':
                calc.append(A+B)
            else: # *인 경우
                calc.append(A*B)
    print('#{} {}'.format(tc, *calc))