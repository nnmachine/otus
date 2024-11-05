# 12.jpg
from math import sqrt


def solution(side: int, r: int):
    for y in range(side):
        for x in range(side):
            print(
                "# " if y <= r and x <= sqrt(r * r - y * y) else ". ",
                end="",
            )

        print()


solution(25, 20)
