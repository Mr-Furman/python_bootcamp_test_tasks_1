import hashlib as hs

s = b"Python Bootcamp"
s_hashing = hs.sha256(s)
print(s_hashing.hexdigest())
