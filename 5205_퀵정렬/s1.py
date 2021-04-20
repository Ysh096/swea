# 파티션과 재귀함수의 두 가지로 나누어 풀기(이해하기)
import sys
sys.stdin = open('input.txt')

# pivot을 가운데에 놓고 L은 오른쪽, R은 왼쪽으로 움직이며
# 각각 pivot보다 큰 값, pivot보다 작은 값을 찾는다.
# 찾은 경우 자리를 교환해준다.
# 찾지 못하고 L과 R이 만난 경우 pivot이 제일 작은 값이 되므로 L와 교환해준다.
# 교환하고 나면 교환한 피봇의 위치는 새로운 피봇이 되고, 양 옆에서 다시 퀵소트!

def quick_sort(a, begin, end):
    if begin < end:
        p = partition(a, begin, end)
        quick_sort(a, begin, p-1)
        quick_sort(a, p+1, end)

def partition(a, begin, end):
    pivot = (begin+end)//2
    L = begin
    R = end
    while L < R:
        while a[L] < a[pivot] and L<R:
            L += 1
        while a[R] >= a[pivot] and L<R:
            R -= 1
        if L < R:
            if L == pivot:
                pivot = R
            a[L], a[R] = a[R], a[L]
    a[pivot], a[R] = a[R], a[pivot]
    return R


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    quick_sort(arr, 0, N-1)
    print("#{} {}".format(tc, arr[N//2]))