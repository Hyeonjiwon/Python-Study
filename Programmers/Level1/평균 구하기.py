import numpy as np

def solution(arr):
    answer = 0
    answer = sum(arr)/len(arr)
    return answer

    # return np.mean(arr) # 속도가 느림

def main():
    arr = [1, 2, 3, 4]

    print(solution(arr))

if __name__ == '__main__':
    main()