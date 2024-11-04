# 10.jpg


def solution(side: int):
    for y in range(side):
        for x in range(side):
            if 0 < (x - y) <= y + 1:
                print("# ", end="")
            else:
                print(". ", end="")
        print()


solution(25)
