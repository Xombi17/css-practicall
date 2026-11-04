# Hill Cipher - encrypt "Dial" with 2x2 key K = [3 3 / 2 5]
# C = (K * P) mod 26, where P is a block of 2 letters as numbers (A=0..Z=25)

key = [[3, 3],
       [2, 5]]

def encrypt(text, key):
    text = text.upper()
    # convert letters to numbers
    nums = [ord(c) - ord('A') for c in text]
    cipher = ""
    # take 2 letters at a time
    for i in range(0, len(nums), 2):
        p1 = nums[i]
        p2 = nums[i + 1]
        c1 = (key[0][0]*p1 + key[0][1]*p2) % 26
        c2 = (key[1][0]*p1 + key[1][1]*p2) % 26
        cipher += chr(c1 + ord('A')) + chr(c2 + ord('A'))
    return cipher

plain = "Dial"
print("Plaintext :", plain)
print("Cipher text:", encrypt(plain, key))
