import math

def is_prime(number):
    return number > 1 and all(number % divisor for divisor in range(2, int(number ** 0.5) + 1))

# RSA public key is (e, n); private key is (d, n).
p, q = map(int, input("Enter two small prime numbers p and q (example: 61 53): ").split())
if p == q or not is_prime(p) or not is_prime(q):
    raise ValueError("Enter two different prime numbers")
n = p * q
phi = (p - 1) * (q - 1)
e = int(input(f"Choose public exponent e coprime with {phi} (example: 17): "))
if not 1 < e < phi or math.gcd(e, phi) != 1:
    raise ValueError("e must be between 1 and phi and coprime with phi")
d = pow(e, -1, phi)

message = int(input(f"Message number (0 to {n - 1}): "))
if not 0 <= message < n:
    raise ValueError("Message must be between 0 and n-1")
ciphertext = pow(message, e, n)
print("Public key (e, n):", (e, n))
print("Private key (d, n):", (d, n))
print("Encrypted message:", ciphertext)
print("Decrypted message:", pow(ciphertext, d, n))
