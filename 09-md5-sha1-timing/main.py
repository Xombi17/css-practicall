import hashlib, time
with open(input("Text file path (use a 1 kB file): "),"rb") as f: data=f.read()
print("Bytes read:",len(data))
for name,make in (("MD5",hashlib.md5),("SHA-1",hashlib.sha1)):
    start=time.perf_counter(); digest=make(data).hexdigest(); elapsed=time.perf_counter()-start
    print(f"{name}: {digest}\nTime: {elapsed:.9f} seconds")
