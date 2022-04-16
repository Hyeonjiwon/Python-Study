nums = [-1,0,3,5,9,12]
target = 9

left, right = 0, len(nums) - 1

while left <= right:
    pivot = (left + right) // 2
    pivot2 = left + (right-left) // 2
    if nums[pivot] == target:
        print(pivot)
    
    if nums[pivot] < target: 
        left = pivot + 1
    else:
        right = pivot - 1
        