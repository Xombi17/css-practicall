# Public p and g are shared; Alice and Bob keep their private numbers secret.
def is_prime(number):
    return number > 1 and all(number % divisor for divisor in range(2, int(number ** 0.5) + 1))

p = int(input("Enter public prime p (example: 23): "))
g = int(input(f"Enter public base g (1 to {p - 1}, example: 5): "))
alice_private = int(input("Enter Alice's private number: "))
bob_private = int(input("Enter Bob's private number: "))
if not is_prime(p) or not 1 <= g < p:
    raise ValueError("p must be prime and g must be between 1 and p-1")

alice_public = pow(g, alice_private, p)
bob_public = pow(g, bob_private, p)
alice_secret = pow(bob_public, alice_private, p)
bob_secret = pow(alice_public, bob_private, p)
print("Alice sends public value:", alice_public)
print("Bob sends public value:", bob_public)
print("Alice computes shared key:", alice_secret)
print("Bob computes shared key:", bob_secret)
