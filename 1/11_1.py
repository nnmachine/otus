def solution(size: int) -> None:
    for y in range(size):
        for x in range(size):
            print(' # ' if (x in [1, 23] or y in [1, 23]) else ' . ', end='')
        print()


solution(25)
