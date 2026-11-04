# Public p and g; Alice and Bob keep their private numbers secret.
p = int(input("Public prime p: "))
g = int(input("Public base g: "))
alice_private = int(input("Alice private number: "))
bob_private = int(input("Bob private number: "))

alice_public = pow(g, alice_private, p)
bob_public = pow(g, bob_private, p)
alice_secret = pow(bob_public, alice_private, p)
bob_secret = pow(alice_public, bob_private, p)
print("Alice public value:", alice_public)
print("Bob public value:", bob_public)
print("Shared secrets:", alice_secret, "and", bob_secret)
