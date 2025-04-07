def euclid(a: int, b: int) -> int:
    if a == b:
        return a
    if a == 0:
        return b
    elif b == 0:
        return a
    print(a, b)
    if a > b:
        return euclid(a % b, b)
    else:
        return euclid(b % a, a)


print(euclid(125, 50))
