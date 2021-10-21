def solution(n):
    answer = []
    answer = list(str(n))
    answer = [int(i) for i in answer]
    answer.reverse()

    return answer

def main():
    n = 131313

    print(solution(n))

if __name__ == '__main__':
    main()