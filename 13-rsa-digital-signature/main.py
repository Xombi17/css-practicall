import hashlib
import math

# Teaching example: hash the message, sign with d, and verify with public key e.
p, q = map(int, input("Enter two small prime numbers p q (example: 61 53): ").split())
n = p * q
phi = (p - 1) * (q - 1)
e = next(value for value in range(2, phi) if math.gcd(value, phi) == 1)
d = pow(e, -1, phi)

message = input("Message to sign: ").encode()
digest = int.from_bytes(hashlib.sha256(message).digest(), "big") % n
signature = pow(digest, d, n)
print("Signature:", signature)
print("Valid:", pow(signature, e, n) == digest)
