# 17.jpg
from math import cos, pi


def solution(side: int):
    for y in range(side):
        for x in range(side):
            print(
                ". " if y <= 9 * cos(x * (pi / 10)) + 14 else "# ",
                end="",
            )
        print()


solution(25)
