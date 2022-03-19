def solution(x):
    arr = list(str(x))
    num = 0

    for i in arr:
        num = num + int(i)

    return True if (x%num) == 0 else False

def main():
    arr = 13

    print(solution(arr))

if __name__ == '__main__':
    main()