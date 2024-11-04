# 23.jpg


def solution(side: int):
    for y in range(side):
        for x in range(side):
            print("# " if y % 3 == 0 and x % 2 == 0 else ". ", end="")
        print()


solution(25)
