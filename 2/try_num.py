def solution(n: int) -> bool:
    for x in range(2, n//2 +1):
        if n % x == 0:
            return False
    return True

print(solution(1))
print(solution(2))
print(solution(3))
print(solution(4))
print(solution(5))
print(solution(6))
print(solution(7))
print(solution(8))
print(solution(9))
print(solution(0))
