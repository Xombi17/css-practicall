import hashlib
import math

# Teaching example: sign a message digest with the private key.
p, q = map(int, input("Enter two small prime numbers p q: ").split())
n = p * q
phi = (p - 1) * (q - 1)
e = next(value for value in range(2, phi) if math.gcd(value, phi) == 1)
d = pow(e, -1, phi)

message = input("Message: ").encode()
digest = int.from_bytes(hashlib.sha256(message).digest(), "big") % n
signature = pow(digest, d, n)
verified_digest = pow(signature, e, n)
print("Signature:", signature)
print("Valid:", verified_digest == digest)
