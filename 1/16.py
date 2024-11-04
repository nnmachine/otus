# 16.jpg


def solution(side: int):
    for y in range(side):
        for x in range(side):
            if (y <= 12 and (15 - y) <= x <= (9 + y)) or (
                y > 12 and (y - 9) <= x <= (33 - y)
            ):
                print("# ", end="")
            else:
                print(". ", end="")
        print()


solution(25)
