import sys
sys.stdin = open('input.txt')

def merge_sort(arr):
    global cnt
    if len(arr) < 2: # 길이가 2 이상이어야 비교가 가능
        # print(arr)
        return arr

    mid = len(arr)//2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    # left, right에는
    # 1) arr = [2, 2] 일 때 left = [2], right = [2]
    # 2) arr = [1, 3] 일 때 left = [1], right = [3]
    # 3) arr = [1, 1, 3] 일 때 left = [1], right = [1, 3] <= right는 정렬된 후
    # 4) arr = [2, 2, 1, 1, 3] 일 때 left = [2, 2], right = [1, 1, 3] <= left, right 정렬된 후임
    # 따라서 배열 left, right 두 개를 비교하여 합친 것을 return 해주면 된다.

    # 일단 문제에서 요구하는 경우의 수를 더해주자.
    if left[-1] > right[-1]:
        cnt += 1

    # left, right 두 배열을 정렬한 후 저장해 줄 배열
    merged = []
    # 정렬(두 배열의 최솟값(왼쪽)에서부터 비교해나간다.)
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] > right[j]: # 오른쪽이 더 작은 경우
            merged.append(right[j]) # 오른쪽 값을 추가해주고
            j += 1 # 오른쪽 값의 다음 위치를 현재 왼쪽 값과 비교
        else:
            merged.append(left[i])
            i += 1
    if i == len(left):
        merged += right[j:]
    else:
        merged += left[i:]
    return merged # return을 해줘야 합친게 left나 right에 저장됨

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    cnt = 0
    arr = merge_sort(arr)

    # print(arr)
    print("#{} {} {}".format(tc, arr[N//2], cnt))