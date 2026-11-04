import math
text=input("Plaintext (letters only): ").upper().replace(" ","")
a,b=map(int,input("Enter keys a b: ").split())
if math.gcd(a,26)!=1: raise ValueError("a must be relatively prime to 26")
print("Ciphertext:","".join(chr((a*(ord(c)-65)+b)%26+65) for c in text))
