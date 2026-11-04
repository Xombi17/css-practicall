import math

# The key must have an inverse modulo 26 so the cipher can be decrypted.
text = input("Plaintext (letters only): ").upper().replace(" ", "")
key = int(input("Key (coprime with 26, e.g. 5): "))
if math.gcd(key, 26) != 1:
    raise ValueError("The key must be relatively prime to 26")

ciphertext = ""
for letter in text:
    value = ord(letter) - ord("A")
    ciphertext += chr((value * key) % 26 + ord("A"))
print("Ciphertext:", ciphertext)
