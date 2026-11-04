import hashlib
import math

p = int(input("Enter p: "))
q = int(input("Enter q: "))

n = p * q
phi = (p-1) * (q-1)

e = int(input("Enter public key e: "))

if math.gcd(e, phi) != 1:
    print("Invalid key")
else:
    d = pow(e, -1, phi)

    message = input("Enter message: ").encode()

    digest = int.from_bytes(hashlib.sha256(message).digest(), "big") % n

    signature = pow(digest, d, n)
    verify = pow(signature, e, n)

    print("Public key:", (e, n))
    print("Private key:", (d, n))
    print("Signature:", signature)
    print("Signature valid:", verify == digest)