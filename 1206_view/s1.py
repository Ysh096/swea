import sys
sys.stdin = open("input.txt", "r")
for i in range(1, 11): #10번 반복
    T = int(input())
    view_list = list(map(int, input().split()))
    # print(view_list)
    result = 0
    for idx in range(2, T-2): #indexError방지, 0이후부터 확인
        m_list = [view_list[idx-2], view_list[idx-1], view_list[idx+1], view_list[idx+2]] #양 옆 두 건물의 높이를 저장
        m_value = 0
        for i in m_list:
            if i >= m_value:
                m_value = i #주변 2개 건물의 높이 최댓값
		#현재 높이 - 주변 건물의 최대 높이
        view_value = view_list[idx] - m_value
        if view_value > 0:
            result += view_value

    print('#{} {}'.format(i, result))


