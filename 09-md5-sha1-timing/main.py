import hashlib
import time

file_path = input("Enter file path: ")

with open(file_path, "rb") as file:
    data = file.read()

print("File size:", len(data), "bytes")

start = time.time()
md5 = hashlib.md5(data).hexdigest()
end = time.time()
print("MD5:", md5)
print("MD5 Time:", end-start)

start = time.time()
sha1 = hashlib.sha1(data).hexdigest()
end = time.time()
print("SHA-1:", sha1)
print("SHA-1 Time:", end-start)

if end-start < end-start:
    print("SHA-1 is faster")
else:
    print("MD5 is faster")