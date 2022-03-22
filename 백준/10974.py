
from itertools import permutations

N = int(input())

data = []
for i in range(1, N+1):
    data.append(i)

result = list(map(list, permutations(data, N)))

for i in result:
    for j in i:
        print(j, end=' ')
    print()

## 재귀로도 풀어보자