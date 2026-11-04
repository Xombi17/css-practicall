text=input("Plaintext: ").upper()
key=input("Keyword (letters only): ").upper()
if not key.isalpha(): raise ValueError("Keyword must contain letters only")
letters=[c for c in text if c.isalpha()]
if not letters: raise ValueError("Enter at least one letter")
ks=(key*(len(letters)//len(key)+1))[:len(letters)]
i=0; out=""
for c in text:
    if c.isalpha(): out+=chr((ord(c)-65+ord(ks[i])-65)%26+65); i+=1
    else: out+=c
print("Ciphertext:",out)
