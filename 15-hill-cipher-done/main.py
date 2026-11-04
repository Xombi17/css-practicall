# Encrypts user-entered text with a user-entered 2x2 Hill key.
key_values = list(map(int, input("Enter the 2x2 key row by row (a b c d): ").split()))
if len(key_values) != 4:
    raise ValueError("Enter exactly four integer values for the 2x2 key")
key = [key_values[:2], key_values[2:]]

def encrypt(text):
    text = text.upper().replace(" ", "")
    if not text.isalpha() or not text.isascii() or len(text) % 2:
        raise ValueError("Enter an even number of A-Z letters")
    numbers = [ord(letter) - 65 for letter in text]
    ciphertext = ""
    for i in range(0, len(numbers), 2):
        x, y = numbers[i], numbers[i + 1]
        c1 = (key[0][0] * x + key[0][1] * y) % 26
        c2 = (key[1][0] * x + key[1][1] * y) % 26
        ciphertext += chr(c1 + 65) + chr(c2 + 65)
    return ciphertext

plaintext = input("Plaintext to encrypt (example: DONE): ")
print("Key matrix:", key)
print("Ciphertext:", encrypt(plaintext))
