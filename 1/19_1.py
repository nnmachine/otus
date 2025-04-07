def solution(size: int) -> None:
    for y in range(size):
        for x in range(size):
            print(' # ' if (x in [0, 24] or y in [0, 24]) else ' . ', end='')
        print()


solution(25)
