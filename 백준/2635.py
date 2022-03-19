n = int(input())

max_list = []

for i in range(int(n/2), n+1):
    tmp_list = [n]
    tmp_list.append(i)

    idx = 1
    while True:
        next_num = tmp_list[idx-1] - tmp_list[idx]
        if next_num < 0:
            break
        tmp_list.append(next_num)
        idx += 1

    if len(max_list) < len(tmp_list):
        max_list = tmp_list

print(len(max_list))
for i in max_list:
    print(i, end= ' ')

# 30864 KB	 80 ms