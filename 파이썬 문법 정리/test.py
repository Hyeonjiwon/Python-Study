<<<<<<< HEAD
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N):
    # write your code in Python 3.6
    arr = list(str(N))
    print(arr.sort())
    print("!!")
    pass


def main():
    n = 213
    print(solution(n))

if __name__ == '__mai__':
    main()
    
=======
import time
from typing import AnyStr
start = time.time()  # 시작 시간 저장

num, base = 444, 5

num = list(str(num))
num = list(map(int, num))

# print(num[::-1])
answer = 0
for i in enumerate(num):
    
    print(i)

"""
answer = 0
for idx, number in enumerate(num[::-1]):
    print(idx, number)
    answer += int(number) * (base ** idx)
"""
print(answer)
# print(int(str(num), base))

print(f"{time.time() - start :.5f}")  # 실행 시간
>>>>>>> a3fbbdafcfa09577fbd5412cf32dff80f228dc30
