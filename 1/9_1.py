def solution(size: int) -> None:
    for y in range(size):
        for x in range(size):
            print(' # ' if abs(x-y) > 10 else ' . ', end='')
        print()


solution(25)
