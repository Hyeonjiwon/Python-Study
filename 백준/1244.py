switch_n = int(input())
state = list(map(int, input().split()))
student_n = int(input())

student = []
for i in range(student_n):
    std = list(map(int, input().split()))
    student.append(std)


for n in range(student_n):
    if student[n][0] == 1:
        for j in range(1, switch_n+1, * student[n][1]):
            if state[j-1] == 0:
                state[j-1] = 1
            else:
                state[j-1] = 0

    if student[n][0] == 2:
        idx = student[n][1] - 1
        if state[idx] == 0:
            state[idx] = 1
        else:
            state[idx] = 0

        for i in range(1, int(switch_n-1/2)):
            if idx - i >= 0 and idx + 1 < switch_n:
                if state[idx - i] == state[idx + i]:
                    if state[idx - i] == 0:
                        state[idx - i] = 1
                        state[idx + i] = 1
                    else:
                        state[idx - i] = 0
                        state[idx + i] = 0
            else:
                break

print(*state, sep=' ')

## 런타임 에러가 났다 
# for문과 if 문으르 줄여보자
# 스위치를 바꾸는 부분은 change 함수로 
# 남자의 경우 배수만 탐색하는 for문으로

# 출력문 조건을 제대로 보지 않았다. 21 번째 부터 다음 줄로

def change(n):
    if state[n] == 0:
        state[n] = 1
    else:
        state[n] = 0
    return

switch_n = int(input())
state = [-1] + list(map(int, input().split()))
student_n = int(input())

for _ in range(student_n):
    sex, num = map(int, input().split())

    if sex == 1:
        for i in range(num, switch_n+1, num):
            change(i)

    else:
        change(num)

        for i in range(switch_n//2):
            if num - i < 1 or num + i > switch_n:
                break
            if state[num - i] == state[num + i]:
                change(num - i)
                change(num + i)
            else:
                break

for i in range(1, switch_n+1):
    print(state[i], end=' ')
    if i % 20 == 0:
        print()
