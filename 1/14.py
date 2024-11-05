# 14.jpg


def solution(side: int, r: int, c: int):
    for y in range(side):
        for x in range(side):
            print(
                "# " if (x - c) ** 2 + (y - c) ** 2 >= r**2 else ". ",
                end="",
            )

        print()


solution(25, 20, 25)
