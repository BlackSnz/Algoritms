def gcd(a, b):
    if a == 0:
        return b
    if b == 0:
        return a
    if a >= b:
        return gcd(a % b, b)
    if b >= a:
        return gcd(a, b % a)
def main():
    print(gcd(3918848, 1653264))

if __name__ == "__main__":
    main()