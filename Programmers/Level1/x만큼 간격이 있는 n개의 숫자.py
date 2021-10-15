import time
start = time.time()  # 시작 시간 저장

def solution(x, n):
    answer = []
    tmp = 0

    for i in range(n):
        tmp = tmp + x
        answer.append(tmp)

    return answer

def main(): 
    print(solution(2, 5))

if __name__ == '__main__':
    main()
    print("time :", time.time() - start)  # 실행 시간
