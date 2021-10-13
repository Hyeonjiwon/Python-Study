def solution(lottos, win_nums):
    if (len(lottos) > 6) or (len(win_nums) > 6):
        raise Exception('Items exceeds the maximum allowed length of 6')

    else:
        answer = []
        dict =  {0:6, 1:6, 2:5, 3:4, 4:3, 5:2, 6:1}
        set_lottos = set(lottos)
        set_winNum = set(win_nums)

        min = len(set_lottos.intersection(set_winNum)) # 교집합
        max = min + lottos.count(0) # 0 개수 count


        return dict.get(max, "?"), dict.get(min, "?")

"""
def switch(key):
    # 맞춘 개수 : 순위
    answer = {1:6, 2:5, 3:4, 4:3, 5:2, 6:1}.get(key, "?")
    return answer
"""

def main():
    # 민우가 구매한 로또 번호
    lottos = [0, 0, 0, 0, 0, 0]
    # 당첨 번호
    win_nums = [38, 19, 20, 40, 15, 25]

    print(solution(lottos, win_nums))


if __name__ == '__main__':
    main()
