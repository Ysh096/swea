import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    primes = [2, 3, 5, 7, 11]
    result = []
    count = 0
    for prime in primes:
        while True:
            if N % prime:
                break
            else:
                N = N/prime
                count += 1
        result.append(count)
        count = 0
    print('#{} {}'.format(tc, ' '.join(map(str, result))))