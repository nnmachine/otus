# 19.jpg


def solution(side: int):
    for y in range(side):
        for x in range(side):
            if x % (side - 1) == 0 or y % (side-1) == 0:
                print("# ", end="")
            else:
                print(". ", end="")
        print()


solution(25)
