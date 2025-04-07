def solution(size: int) -> None:
    for y in range(size):
        for x in range(size):
            print(' # ' if (x + y) <= 29 else ' . ', end='')
        print()


solution(25)
