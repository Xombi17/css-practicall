import math

# Small classroom RSA: n=p*q, phi=(p-1)(q-1), and d is inverse of e modulo phi.
p, q = map(int, input("Enter two small prime numbers p q (example: 61 53): ").split())
n = p * q
phi = (p - 1) * (q - 1)
e = next(value for value in range(2, phi) if math.gcd(value, phi) == 1)
d = pow(e, -1, phi)

message = int(input(f"Message number (0 to {n - 1}): "))
if not 0 <= message < n:
    raise ValueError("Message must be between 0 and n-1")
ciphertext = pow(message, e, n)
print("Public key:", (e, n))
print("Private key:", (d, n))
print("Encrypted:", ciphertext)
print("Decrypted:", pow(ciphertext, d, n))
