# 24.jpg


def solution(side: int):
    for y in range(side):
        for x in range(side):
            if (x + y) + 1 == side or x == y:
                print("# ", end="")
            else:
                print(". ", end="")
        print()


solution(25)
