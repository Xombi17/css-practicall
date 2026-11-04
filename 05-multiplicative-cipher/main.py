text=input("Plaintext (letters only): ").upper().replace(" ","")
a=int(input("Key a (coprime with 26): "))
if __import__('math').gcd(a,26)!=1: raise ValueError("Key must be relatively prime to 26")
print("Ciphertext:","".join(chr(((ord(c)-65)*a)%26+65) for c in text))
