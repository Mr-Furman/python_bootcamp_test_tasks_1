import hashlib as hs

s_1 = b"Python Bootcamp"
s_hashing_variant_1 = hs.md5(s_1)

print('Variant 1:',s_hashing_variant_1.hexdigest())


s_2 = b"Python Bootcamp"
s_hashing_variant_2 = hs.sha256(s_2)
print('Variant 2:',s_hashing_variant_2.hexdigest())
