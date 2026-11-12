def gcd(a, b):
    while b:
        a, b = b, a % b
    return abs(a)


assert gcd(48, 18) == 6 and gcd(7, 0) == 7 and gcd(0, 0) == 0

if __name__ == "__main__":
    a = int(input("A: "))
    b = int(input("B: "))
    print(gcd(a, b))
