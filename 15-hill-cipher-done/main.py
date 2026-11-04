values = input("Enter 4 key values: ").split()
a = int(values[0])
b = int(values[1])
c = int(values[2])
d = int(values[3])
key = [[a, b], [c, d]]
def encrypt(text):
    text = text.upper().replace(" ", "")
    if not text.isalpha() or not text.isascii() or len(text) % 2 != 0:
        print("Enter even number of letters")
        return ""
    cipher = ""
    for i in range(0, len(text), 2):
        x = ord(text[i]) - 65
        y = ord(text[i+1]) - 65
        c1 = (a*x + b*y) % 26
        c2 = (c*x + d*y) % 26
        cipher += chr(c1+65) + chr(c2+65)
    return cipher
plain = input("Enter plaintext: ")
print("Key matrix:", key)
print("Ciphertext:", encrypt(plain))