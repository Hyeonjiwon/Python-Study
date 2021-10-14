import time
start = time.time()  # 시작 시간 저장

import re

def solution(new_id):
    # 배열 길이
    if (len(new_id) < 0) or (len(new_id) > 1000):
        raise Exception('Items exceeds the maximum allowed length')

    # 1
    new_id = new_id.lower()
    
    # 2
    new_id = re.sub('[^0-9a-z\-_.]', '', new_id)

    # 3
    new_id = re.sub('[.]{1,}', '.', new_id)
    
    # 4
    if len(new_id) >= 2:
        if new_id.startswith('.'):
            new_id = new_id[1:]

    if new_id.endswith('.'):
        new_id = new_id[:-1]

    # 5
    if not new_id:
        new_id = new_id.replace("", "a")

    # 6
    if len(new_id) > 15:
        new_id = new_id[:15]

        if new_id.endswith('.'):
            new_id = new_id[:-1]
    
    # 7 
    #while len(new_id) < 3:
    #    new_id = new_id + new_id[-1]

    new_id+=new_id[-1]*(3-len(new_id))

    return new_id



def main():
    id = "...!@BaT#*..y.abcdefghijklm"    

    print(solution(id))

if __name__ == '__main__':
    main()
    print("time :", time.time() - start)  # 현재시각 - 시작시간 = 실행 시간
