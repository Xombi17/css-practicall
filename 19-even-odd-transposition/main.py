# Positions in the question are counted from 1, so index 1 is an even position.
text = input("Plaintext: ")
even_positions = text[1::2]
odd_positions = text[::2]
print("Ciphertext:", even_positions + odd_positions)
