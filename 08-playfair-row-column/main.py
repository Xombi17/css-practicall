key=input("Keyword: ").upper().replace("J","I")
text=input("Plaintext (even number of letters): ").upper().replace("J","I").replace(" ","")
alphabet="ABCDEFGHIKLMNOPQRSTUVWXYZ"
square="".join(dict.fromkeys(key+alphabet))
if len(text)%2 or not text.isalpha(): raise ValueError("Enter an even number of letters only")
for a,b in zip(text[::2],text[1::2]):
    r1,c1=divmod(square.index(a),5); r2,c2=divmod(square.index(b),5)
    if r1==r2: a,b=square[r1*5+(c1+1)%5],square[r2*5+(c2+1)%5]
    elif c1==c2: a,b=square[((r1+1)%5)*5+c1],square[((r2+1)%5)*5+c2]
    print(a+b,end="")
print()
