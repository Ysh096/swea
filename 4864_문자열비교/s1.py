str1 = 'iss'
str2 = 'This iss a sentence'
def 브루트포스1(p, t):
    for i in range(len(t)-len(p)+1):
        #패턴의 길이만큼 반복
        is_ok = True
        for j in range(len(p)):
            if p[j] != t[i+j]:
                is_ok = False
                break

        if is_ok:
            return 1
    return 0

print(브루트포스1(str1, str2))

def 브루트포스2(p, t):
    i = 0 #t텍스트를 컨트롤 하는 인덱스
    j = 0 #p패턴을 컨트롤 하는 인덱스

    #j가 패턴의 길이가 된다면 찾았다면 멈춘다.
    #i가 텍스트의 길이가 된다면 멈춘다.
    while j < len(p) and i < len(t):
        if p[j] != t[i]:
            i = i-j
            j = -1

        i+=1
        j+=1

    if j == len(p): return 1

str1 = 'iss'
str2 = 'This iss a sentence'
print(브루트포스2(str1, str2))
