# 11.jpg
from math import sqrt


def solution(side: int, r: int):
    for y in range(side):
        for x in range(side):
            if y > r:
                print(". ", end="")
            else:
                print("# " if x <= sqrt(r * r - y * y) else ". ", end="")

        print()


solution(25, 20)
