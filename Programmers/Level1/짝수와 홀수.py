def solution(arr):
    if len(arr)==1:
        answer = [-1]
        return answer

    else:
        arr.remove(min(arr))
        return arr

def main():
    arr = [10]
    print(solution(arr))

if __name__ == '__main__':
    main()
    