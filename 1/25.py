# 25.jpg


def solution(side: int):
    for y in range(side):
        for x in range(side):
            if x % 6 == 0 or y % 6 == 0:
                print("# ", end="")
            else:
                print(". ", end="")
        print()


solution(25)
