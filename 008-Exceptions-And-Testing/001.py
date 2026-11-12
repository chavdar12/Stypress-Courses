import math


class SameSignError(ValueError):
    pass


def f(x):
    return math.exp(x) - 2 * x - 2


def bisection(func, a, b, eps=0.001):
    fa, fb = func(a), func(b)
    if fa * fb > 0:
        raise SameSignError(f"f({a}) and f({b}) have the same sign")
    while b - a > eps:
        c = (a + b) / 2
        fc = func(c)
        if fc == 0:
            return c
        if fa * fc < 0:
            b = c
        else:
            a, fa = c, fc
    return (a + b) / 2


def read_number(prompt):
    text = input(prompt)
    try:
        return float(text)
    except ValueError:
        raise ValueError(f"'{text}' is not a number") from None


# lecture example: x^3 + 3x - 5 on [1, 2] -> 1.154
assert abs(bisection(lambda x: x ** 3 + 3 * x - 5, 1, 2) - 1.154) < 0.001
assert abs(f(bisection(f, 1, 2, 1e-9))) < 1e-6
try:
    bisection(f, 2, 3)
    assert False
except SameSignError:
    pass

if __name__ == "__main__":
    try:
        a = read_number("a: ")
        b = read_number("b: ")
        print(f"Root: {bisection(f, a, b):.4f}")
    except ValueError as error:
        print("Error:", error)
