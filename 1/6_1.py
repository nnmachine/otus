def solution(size: int) -> None:
    for y in range(size):
        for x in range(size):
            print(' . ' if (x>15 and y>15) else ' # ', end='')
        print()


solution(25)
