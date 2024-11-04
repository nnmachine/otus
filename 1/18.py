# 18.jpg


def solution(side: int):
    for y in range(side):
        for x in range(side):
            print(
                "# " if (x or y) and (x * y == x or x * y == y) else ". ",
                end="",
            )
        print()


solution(25)
