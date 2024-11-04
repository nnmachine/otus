# 19.jpg


def solution(side: int):
    for y in range(side):
        for x in range(side):
            print("# " if not ((x + y) % 2) else ". ", end="")
        print()


solution(25)
