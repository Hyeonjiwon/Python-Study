import time
start = time.time()  # 시작 시간 저장

def solution(lottos, win_nums):
    # 배열 길이가 6보다 클 경우
    if (len(lottos) > 6) or (len(win_nums) > 6):
        raise Exception('Items exceeds the maximum allowed length of 6')

    else:
        answer = []
        # 맞춘 개수 : 순위
        dict =  {0:6, 1:6, 2:5, 3:4, 4:3, 5:2, 6:1}
        set_lottos = set(lottos)
        set_winNum = set(win_nums)

        min = len(set_lottos.intersection(set_winNum)) # 교집합
        max = min + lottos.count(0) # 0 개수 count

        # max = len(set(lottos) & set(win_nums)) + lottos.count(0)
        # min = len(set(lottos) & set(win_nums))

        return [dict.get(max, "?"), dict.get(min, "?")] # time : 0.0006847381591796875
        # return [dict[max], dict[min]] # time : 0.0009970664978027344

"""
def switch(key):
    # 맞춘 개수 : 순위
    answer = {1:6, 2:5, 3:4, 4:3, 5:2, 6:1}.get(key, "?")
    return answer
"""

def main():
    # 민우가 구매한 로또 번호
    lottos = [44, 1, 0, 0, 31, 25]
    # 당첨 번호
    win_nums = [31, 10, 45, 1, 6, 19]
    
    print(solution(lottos, win_nums))


if __name__ == '__main__':
    main()
    print("time :", time.time() - start)  # 현재시각 - 시작시간 = 실행 시간
