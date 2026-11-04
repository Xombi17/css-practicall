import hashlib, getpass, secrets
password=getpass.getpass("Password: ").encode()
salt=secrets.token_bytes(16)
pepper=getpass.getpass("Pepper (secret): ").encode()
digest=hashlib.sha256(salt+password+pepper).hexdigest()
print("Salt (store with hash):",salt.hex())
print("SHA-256:",digest)
