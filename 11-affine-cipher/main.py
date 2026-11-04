import math

# E(x) = (a*x + b) mod 26; a must have an inverse modulo 26.
text = input("Plaintext (letters only): ").upper().replace(" ", "")
a, b = map(int, input("Enter keys a b (example: 5 8): ").split())
if math.gcd(a, 26) != 1:
    raise ValueError("Key a must be relatively prime to 26")

ciphertext = ""
for letter in text:
    value = ord(letter) - 65
    ciphertext += chr((a * value + b) % 26 + 65)
print("Ciphertext:", ciphertext)
