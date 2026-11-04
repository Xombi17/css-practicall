text=input("Plaintext (letters only): ").upper().replace(" ","")
key=input("Key, same number of letters: ").upper().replace(" ","")
if len(text)!=len(key) or not text.isalpha() or not key.isalpha(): raise ValueError("Use letters only and a key of equal length")
print("Ciphertext:","".join(chr(((ord(p)-65+ord(k)-65)%26)+65) for p,k in zip(text,key)))
