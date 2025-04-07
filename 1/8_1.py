def solution(size: int) -> None:
    for y in range(size):
        for x in range(size):
            print(' # ' if (x==0 or y==0) else ' . ', end='')
        print()


solution(25)
