import math

def encrypt(text, key):
    result = ""
    for letter in text.upper():
        if "A" <= letter <= "Z":
            value = ord(letter) - 65
            result += chr((value * key) % 26 + 65)
        else:
            result += letter
    return result

def decrypt(text, key):
    inverse = pow(key, -1, 26)
    return encrypt(text, inverse)

plaintext = input("Plaintext: ")
key = int(input("Key coprime with 26 (example: 5): ")) % 26
if math.gcd(key, 26) != 1:
    raise ValueError("The key must be relatively prime to 26")
ciphertext = encrypt(plaintext, key)
print("Ciphertext:", ciphertext)
print("Decrypted:", decrypt(ciphertext, key))
