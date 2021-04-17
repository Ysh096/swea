import sys
sys.stdin = open('input.txt')

# 송금할 금액
# 2진수 or 3진수
# 1010 212
# 자릿수는 3 <= x < 40

T = int(input())

for tc in range(1, T+1):
    # 데이터 받아오기
    bin_val = list(input())
    ter_val = list(input())

    # 이진수 각 자리를 하나씩 바꿈
    for i in range(len(bin_val)):
        temp_bin = list(bin_val)
        if bin_val[i] == '1':
            temp_bin[i] = '0'
        else:
            temp_bin[i] = '1'
        # 바꾼 값의 3진수 표현이 어떤지 확인해보자.
        dec = int(''.join(temp_bin), 2)
        result = int(dec)
        a = dec // 3
        if a == 0:
            ter = '0' * (len(ter_val)-1) + str(dec % 3) # 2라면 002로 표현하기 위함
        else:
            ter = ''
            while a > 0:
                a, b = divmod(dec, 3)
                dec = a
                ter = str(b) + ter
            if len(ter) != len(ter_val):
                ter = '0' * (len(ter_val) - len(ter)) + ter # 22라면 022가 되도록 길이 맞춰줌
        # ter에는 3진수 값이 들어있음
        # 받아온 ter_val과 ter을 비교해서 2개 일치하면 답!
        cnt = 0
        for idx, val in enumerate(ter_val):
            if val == ter[idx]:
                cnt += 1
        if cnt == len(ter_val)-1:
            print('#{} {}'.format(tc, result))
            break