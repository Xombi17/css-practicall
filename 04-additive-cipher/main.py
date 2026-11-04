text=input("Plaintext: ").upper()
k=int(input("Additive key: "))%26
print("Ciphertext:","".join(chr((ord(c)-65+k)%26+65) if c.isalpha() else c for c in text))
