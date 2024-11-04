# 15.jpg


def solution(side: int):
    for y in range(side):
        for x in range(side):
            if (20 >= x - y >= 10) or (20 >= y - x >= 10):
                print("# ", end="")
            else:
                print(". ", end="")
        print()


solution(25)
