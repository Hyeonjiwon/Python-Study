def solution(participant, completion):
    participant.sort()
    completion.sort()

    for p,c in zip(participant, completion):
        # print(p, c)
        if p != c:
            return p

    return participant.pop()

def main():
    participant = ["mislav", "stanko", "mislav", "ana"]
    completion = ["stanko", "ana", "mislav"]

    print(solution(participant, completion))

if __name__ == '__main__':
    main()
    