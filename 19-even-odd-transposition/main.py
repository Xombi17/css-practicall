def encrypt(text):
    even_positions = text[1::2]
    odd_positions = text[::2]
    return even_positions + odd_positions

plaintext = input("Plaintext: ")
print("Ciphertext:", encrypt(plaintext))
