# 04.jpg


def solution(side: int, limit: int) -> None:
    for y in range(side):
        for x in range(side):
            print("# " if (x + y) < limit else ". ", end="")
        print()


solution(25, 30)
