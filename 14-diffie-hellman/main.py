def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return n > 1

p = int(input("Enter prime p: "))
g = int(input("Enter base g: "))

a = int(input("Enter Alice's private key: "))
b = int(input("Enter Bob's private key: "))

if not is_prime(p) or not 1 <= g < p:
    print("Invalid values")
else:
    A = pow(g, a, p)
    B = pow(g, b, p)

    alice_secret = pow(B, a, p)
    bob_secret = pow(A, b, p)

    print("Alice public key:", A)
    print("Bob public key:", B)
    print("Alice shared key:", alice_secret)
    print("Bob shared key:", bob_secret)