w, h = map(int, input().split())
N = int(input())

width = [w]
height = [h]

for _ in range(N):
    v, n = map(int, input().split())

    if v == 0:
        height.append(n)

    else:
        width.append(n)

height.sort()
width.sort()

new_width = [width[0]]
new_height = [height[0]]

for i in range(len(width)-1, 0, -1):
    new_width.append(width[i] - width[i-1])

for i in range(len(height)-1, 0, -1):
    new_height.append(height[i] - height[i-1])

print(max(new_width) * max(new_height))

## 어렵게 생각하지 말자 !!