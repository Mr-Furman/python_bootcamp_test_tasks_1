import hashlib as hs

s = b"Python Bootcamp"
s_hashing = hs.md5(s)

print(s_hashing.hexdigest())
