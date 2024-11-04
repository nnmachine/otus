# 11.jpg


def solution(side: int, radius: int):
    for y in range(side):
        for x in range(side):
            if x in [1, side - 2] or y in [1, side - 2]:
                print("# ", end="")
            else:
                print(". ", end="")
        print()


solution(25, 21)
