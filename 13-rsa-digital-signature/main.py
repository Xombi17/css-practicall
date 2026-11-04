import hashlib
import math

def is_prime(number):
    return number > 1 and all(number % divisor for divisor in range(2, int(number ** 0.5) + 1))

# The signer chooses e; d is computed as its inverse modulo phi.
p, q = map(int, input("Enter two small prime numbers p and q (example: 61 53): ").split())
if p == q or not is_prime(p) or not is_prime(q):
    raise ValueError("Enter two different prime numbers")
n = p * q
phi = (p - 1) * (q - 1)
e = int(input(f"Choose public exponent e coprime with {phi} (example: 17): "))
if not 1 < e < phi or math.gcd(e, phi) != 1:
    raise ValueError("e must be between 1 and phi and coprime with phi")
d = pow(e, -1, phi)

message = input("Message to sign: ").encode()
digest = int.from_bytes(hashlib.sha256(message).digest(), "big") % n
signature = pow(digest, d, n)
verified_digest = pow(signature, e, n)
print("Public key (e, n):", (e, n))
print("Private key (d, n):", (d, n))
print("Signature:", signature)
print("Signature valid:", verified_digest == digest)
