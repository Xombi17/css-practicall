# A=0 through Z=25. The key must be as long as the plaintext.
text = input("Plaintext (letters only): ").upper().replace(" ", "")
key = input("Key (same number of letters): ").upper().replace(" ", "")
if len(text) != len(key) or not text.isalpha() or not key.isalpha():
    raise ValueError("Use letters only and a key of equal length")

ciphertext = ""
for plain_letter, key_letter in zip(text, key):
    value = (ord(plain_letter) - 65 + ord(key_letter) - 65) % 26
    ciphertext += chr(value + 65)
print("Ciphertext:", ciphertext)
