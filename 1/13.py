# 13.jpg


def solution(side: int):
    for y in range(side):
        for x in range(side):
            if (x + y < 20) or (x + y > 28):
                print(". ", end="")
            else:
                print("# ", end="")
        print()


solution(25)
