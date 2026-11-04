# A=0 through Z=25; shifting past Z wraps back to A.
text = input("Plaintext: ").upper()
shift = int(input("Shift: ")) % 26
ciphertext = ""
for letter in text:
    if "A" <= letter <= "Z":
        ciphertext += chr((ord(letter) - ord("A") + shift) % 26 + ord("A"))
    else:
        ciphertext += letter
print("Ciphertext:", ciphertext)
