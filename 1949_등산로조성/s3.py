import sys
sys.stdin = open('input.txt')
a = input()
a = input()
test = [list(map(int, input().split())) for _ in range(5)]

print(max(test))

# 2차원 리스트에 max를 사용하면 2차원 리스트의 원소 리스트의 각 원소! 를
# 서로 비교하여 가장 큰 순서를 가지는 리스트 원소를 출력해준다.
