import sys
sys.stdin = open('input.txt', encoding='UTF8')
for _ in range(10):
    tc = int(input())
    keyword = input()
    sen = input()
    cnt = 0
    fc = keyword[0] #first character
    L = len(keyword) #keyword length
    i = 0
    while i < len(sen):
        if fc == sen[i]:
            if keyword == sen[i:i+L]:
                cnt += 1
                i += L
            else:
                i += 1
        else:
            i += 1

    print('#{} {}'.format(tc, cnt))
