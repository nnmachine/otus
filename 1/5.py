# 05.jpg


def solution(side: int, limit: int) -> None:
    limit_ = limit
    next_x = 0
    for y_ in range(side):
        for x_ in range(side):
            if limit_ and x_ == next_x:
                print("# ", end="")
                limit_ -= 1
                next_x += 1
            else:
                print(". ", end="")
        print()
        limit_ = limit


solution(25, 2)
