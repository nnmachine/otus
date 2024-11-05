# 12.jpg
from math import sqrt


def solution(side: int, r: int):
    for y in range(side):
        for x in range(side):
            print(
                "# " if x**2 + y**2 <= r**2 else ". ",
                end="",
            )

        print()


solution(25, 20)
