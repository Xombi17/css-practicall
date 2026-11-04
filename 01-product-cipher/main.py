text=input("Plaintext (letters only): ").upper().replace(" ","")
shift=int(input("Substitution shift: "))%26
sub="".join(chr((ord(c)-65+shift)%26+65) for c in text)
cols=4
pad=sub+"X"*((-len(sub))%cols)
cipher="".join(pad[i::cols] for i in range(cols))
print("After substitution:",sub)
print("Product cipher:",cipher)
