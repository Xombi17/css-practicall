import hashlib, math
p,q=map(int,input("Enter two small prime numbers p q: ").split())
n=p*q; phi=(p-1)*(q-1)
e=next(x for x in range(2,phi) if math.gcd(x,phi)==1); d=pow(e,-1,phi)
message=input("Message: ").encode()
h=int.from_bytes(hashlib.sha256(message).digest(),"big")%n
sig=pow(h,d,n)
print("Signature:",sig)
print("Valid:",pow(sig,e,n)==h)
