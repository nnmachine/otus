# 08.jpg


def solution(side: int):
    for y in range(side):
        for x in range(side):
            if not x or not y:
                print("# ", end="")
            else:
                print(". ", end="")
        print()


solution(25)
