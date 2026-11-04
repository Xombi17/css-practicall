import math
p = int(input("Enter prime number p: "))
q = int(input("Enter prime number q: "))
n = p * q
phi = (p-1) * (q-1)
e = 2
while e < phi:
    if math.gcd(e, phi) == 1:
        break
    e += 1
d = pow(e, -1, phi)
message = int(input("Enter message: "))
cipher = pow(message, e, n)
decrypt = pow(cipher, d, n)
print("Public key:", (e, n))
print("Private key:", (d, n))
print("Encrypted message:", cipher)
print("Decrypted message:", decrypt)