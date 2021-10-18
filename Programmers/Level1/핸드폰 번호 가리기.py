def solution(phone_number):
    answer = list(phone_number)

    for i in range(len(answer)-4):
        answer[i] = "*" 

    return ''.join(answer)

def main():
    phone_number = "027778888"
    print(solution(phone_number))

if __name__ == '__main__':
    main()
    