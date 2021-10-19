def solution(num):
    answer = 0

    while num > 1:
        if num % 2 == 0:
            num = num/2

        else:
            num = (num * 3) + 1

        if (answer <= 500):
            answer = (answer + 1) 
    
        else: 
            return -1
        
    return answer

def main():
    arr = 1
    print(solution(arr))

if __name__ == '__main__':
    main()