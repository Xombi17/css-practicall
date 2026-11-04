# Hill Cipher - encrypt "Done" with 2x2 key K = [5 2 / 3 3]
# C = (K * P) mod 26 , two letters at a time (A=0..Z=25)

key = [[5, 2],
       [3, 3]]

def encrypt(text, key):
    text = text.upper()
    nums = [ord(c) - ord('A') for c in text]
    cipher = ""
    for i in range(0, len(nums), 2):
        p1 = nums[i]
        p2 = nums[i + 1]
        c1 = (key[0][0]*p1 + key[0][1]*p2) % 26
        c2 = (key[1][0]*p1 + key[1][1]*p2) % 26
        cipher += chr(c1 + ord('A')) + chr(c2 + ord('A'))
    return cipher

plain = "Done"
print("Plaintext :", plain)
print("Cipher text:", encrypt(plain, key))
