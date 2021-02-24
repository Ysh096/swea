import sys
sys.stdin = open('input.txt')
#괄호 '('는 무조건 넣어주고, 스택 안에서 '('가 앞에 있으면 신경쓰지 않는다.
#괄호 ')'를 만나면 '('를 만날 때 까지 pop해서 출력하고, '('은 버린다.
#+-끼리 만나면 앞의 것을 pop해서 출력하고 뒤의 것은 스택에 쌓는다.
#*/끼리 만나면 앞의 것을 pop해서 출력하고 뒤의 것은 스택에 쌓는다.
for tc in range(1, 11):
    Len = int(input())
    string = input()

    #1. 후위연산자 형식으로 바꾸기
    stack = []
    result = ''
    op = {'+': 1, '*': 2} #연산자 우선순위
    #연산자는 +, * 두 개
    #숫자는 0~9
    #*가 +를 만나면 push, +가 *를 만나면 +를 만날때까지 pop하고 뒤에 써주기
    for val in string:
        if val in op:
            while stack:
                if op[val] > op[stack[-1]]: #*앞에 +가 있는 경우
                    stack.append(val)
                    break
                elif op[val] < op[stack[-1]]: #+앞에 *가 있는 경우
                    result += stack.pop()
                else: #+앞에 +가 있는 경우
                    result += stack.pop()
                    stack.append(val) #앞을 꺼내고 자기가 들어감
                    break
            else: #스택이 비어있는 경우
                stack.append(val)
        else: #숫자를 만나면
            result += val
    #for문이 끝나고 나면 stack에서 꺼내지 못한 연산자들이 있다. 이걸 추가해주자.
    while stack:
        result += stack.pop()
    # print(result)

    #2. 계산하기
    #숫자면 스택에 쌓기
    #연산자면 스택에서 피연산자 두개를 꺼내서 계산한 후 스택에 넣기
    calc = [] #숫자를 넣을 배열
    for val in result:
        if val in op: #연산자인 경우
            if val == '+': #어쩔수없이 수작업 해야할듯??
                B = calc.pop()
                A = calc.pop()
                calc.append(A + B)
            elif val == '*':
                B = calc.pop()
                A = calc.pop()
                calc.append(A * B)
        else: #숫자인 경우
            calc.append(int(val))

    print('#{} {}'.format(tc, *calc))