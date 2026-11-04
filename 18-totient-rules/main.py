# Euler's Totient function - first 3 rules
# Rule 1: phi(1) = 0
# Rule 2: phi(p) = p - 1   if p is prime
# Rule 3: phi(m*n) = phi(m) * phi(n)   if m and n are coprime

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def phi(n):
    # Rule 1
    if n == 1:
        return 0
    # Rule 2
    if is_prime(n):
        return n - 1
    # Rule 3: split n into m * k where m and k are coprime
    for m in range(2, n):
        if n % m == 0:
            k = n // m
            if gcd(m, k) == 1:
                return phi(m) * phi(k)
    # fallback (count numbers coprime with n)
    count = 0
    for i in range(1, n):
        if gcd(i, n) == 1:
            count += 1
    return count

n = int(input("Enter a number: "))
if n < 1:
    raise ValueError("Enter a positive integer")
print("phi(", n, ") =", phi(n))
