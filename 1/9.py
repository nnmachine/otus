# 09.jpg


def solution(side: int):
    for y in range(side):
        for x in range(side):
            print("# " if abs(y - x) > 10 else ". ", end="")
        print()


solution(25)
