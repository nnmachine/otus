def solution(size: int) -> None:
    for y in range(size):
        for x in range(size):
            print(' # ' if 0 < x-y <= 1+y else ' . ', end='')
        print()


solution(25)
