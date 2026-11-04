import hashlib
import time

# A hash is a fixed-length fingerprint of file bytes; it is not encryption.
file_path = input("Path to the 1 KiB text file: ")
with open(file_path, "rb") as file:
    data = file.read()
print(f"File size: {len(data)} bytes (1 KiB = 1024 bytes)")
if len(data) != 1024:
    print("Note: this file is not exactly 1 KiB, so the comparison uses its actual size.")

results = []
for name, hash_function in (("MD5", hashlib.md5), ("SHA-1", hashlib.sha1)):
    start = time.perf_counter()
    digest = hash_function(data).hexdigest()
    elapsed = time.perf_counter() - start
    results.append((name, elapsed))
    print(f"\n{name} digest (the file fingerprint): {digest}")
    print(f"Time to calculate it: {elapsed:.9f} seconds")
print(f"\nFaster in this single run: {min(results, key=lambda item: item[1])[0]}")
print("One run is noisy; repeat the experiment for a fairer timing comparison.")
