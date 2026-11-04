import hashlib
import os
PEPPER = "mysecretpepper"   # secret, never stored with the hash
def make_salt():
    return os.urandom(8).hex()   # random salt as text
def hash_password(password, salt):
    mix = salt + password + PEPPER
    return hashlib.sha256(mix.encode()).hexdigest()
password = input("Enter password: ")
salt = make_salt()
stored = hash_password(password, salt)
print("Salt (stored in DB):", salt)
print("Hash (stored in DB):", stored)
again = input("Re-enter password to verify: ")
if hash_password(again, salt) == stored:
    print("Password correct")
else:
    print("Password wrong")
