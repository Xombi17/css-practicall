# 13. RSA digital signature (toy)

**Language:** Python

## Idea

Hashes the message with SHA-256 using Python hashlib, reduces the digest modulo the toy RSA modulus, signs with the private exponent, and verifies with the public exponent. Real RSA signatures require secure padding and large keys; this is only a classroom example.

## Run

Run with `python main.py`.
