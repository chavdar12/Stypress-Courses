import math


def solve(a, b, c):
    if a != 0:
        d = b * b - 4 * a * c
        if d < 0:
            return "No real roots"
        x1 = (-b + math.sqrt(d)) / (2 * a)
        x2 = (-b - math.sqrt(d)) / (2 * a)
        return (x1,) if d == 0 else (x1, x2)
    if b != 0:
        return (-c / b,)
    return "Any x is a root" if c == 0 else "No roots"


assert solve(1, -3, 2) == (2.0, 1.0)
assert solve(1, 2, 1) == (-1.0,)
assert solve(1, 0, 1) == "No real roots"
assert solve(0, 2, -4) == (2.0,)
assert solve(0, 0, 0) == "Any x is a root" and solve(0, 0, 5) == "No roots"

if __name__ == "__main__":
    a, b, c = (float(input(f"{n}: ")) for n in "abc")
    print(solve(a, b, c))
