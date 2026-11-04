# The additive cipher adds the key to each letter value modulo 26.
text = input("Plaintext: ").upper()
key = int(input("Additive key: ")) % 26
ciphertext = ""
for letter in text:
    if "A" <= letter <= "Z":
        value = ord(letter) - ord("A")
        ciphertext += chr((value + key) % 26 + ord("A"))
    else:
        ciphertext += letter
print("Ciphertext:", ciphertext)
