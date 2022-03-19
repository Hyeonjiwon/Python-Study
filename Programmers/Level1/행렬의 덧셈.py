def solution(arr1, arr2):
    answer = [[j for j in range(len(arr1[0]))] for i in range(len(arr1))]

    for i in range(len(arr1)):
        for j in range(len(arr1[i])):
            answer[i][j] = arr1[i][j] + arr2[i][j]

    return answer


def main():
    arr1 = [[1,2], [2,3]]
    arr2 = [[3,4], [5,6]]

    print(solution(arr1, arr2))

if __name__ == '__main__':
    main()
    