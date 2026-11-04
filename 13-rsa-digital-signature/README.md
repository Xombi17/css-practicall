# 13. RSA digital signature (toy)

**Language:** Python

## Idea

Hashes the message with built-in SHA-256, reduces the result to this toy key’s range, signs with the private exponent and verifies with the public exponent. This is for learning only; real RSA signatures need secure padding and a vetted library.

## Run

Run with `python main.py`.
