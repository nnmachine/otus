def pow(x: int, n: float) -> float:
    if n == 0.0:
        return 1
    print(x, n)
    r = pow(x, n // 2)
    if n % 2:
        return x * r * r
    else:
        return r * r


print(pow(2, 10))
