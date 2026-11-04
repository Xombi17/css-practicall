text=input("Plaintext: ").upper().replace(" ","")
cols=4; text+="X"*((-len(text))%cols)
print("Ciphertext:","".join(text[i::cols] for i in range(cols)))
