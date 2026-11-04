# A=0 through Z=25. The key must be as long as the plaintext.
text = input("Plaintext (example: HELLO): ").upper().replace(" ", "")
key = input("Text key (same length, example: CLASS): ").upper().replace(" ", "")
if len(text) != len(key) or not all("A" <= letter <= "Z" for letter in text + key):
    raise ValueError("Use letters only and a key of equal length")

ciphertext = ""
for plain_letter, key_letter in zip(text, key):
    value = (ord(plain_letter) - 65 + ord(key_letter) - 65) % 26
    ciphertext += chr(value + 65)
print("Ciphertext:", ciphertext)
print("Reuse the same key and subtract its letter values to decrypt.")
