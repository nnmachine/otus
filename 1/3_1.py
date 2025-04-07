def solution(size: int) -> None:
    for y in range(size):
        for x in range(size):
            print(' # ' if (x + y) + 1 == size else ' . ', end='')
        print()


solution(25)
