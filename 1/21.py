# 21.jpg


def solution(side: int):
    for y in range(side):
        for x in range(side):
            print("# " if x % (y + 1) == 0 else ". ", end="")
        print()


solution(25)
