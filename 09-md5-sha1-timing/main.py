import hashlib
import time

# Read bytes so the file's text encoding does not change the data being hashed.
file_path = input("Text file path (use a 1 kB file): ")
with open(file_path, "rb") as file:
    data = file.read()
print("Bytes read:", len(data))

for name, hash_function in (("MD5", hashlib.md5), ("SHA-1", hashlib.sha1)):
    start = time.perf_counter()
    digest = hash_function(data).hexdigest()
    elapsed = time.perf_counter() - start
    print(f"{name}: {digest}")
    print(f"Time: {elapsed:.9f} seconds")
