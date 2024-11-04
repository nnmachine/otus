# 02.jpg


def solution(side: int):
    for y in range(side):
        for x in range(side):
            print("# " if x == y else ". ", end="")
        print()


solution(25)
