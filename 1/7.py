# 07.jpg


def solution(side: int, small_side: int) -> None:
    for y in range(side):
        for x in range(side):
            if side - x <= small_side and side - y <= small_side:
                print("# ", end="")
            else:
                print(". ", end="")
        print()


solution(25, 9)
