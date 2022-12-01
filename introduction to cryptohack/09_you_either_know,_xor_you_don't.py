# I've encrypted the flag with my secret key, you'll never be able to guess it.

# Remember the flag format and how it might help you in this challenge!

# 0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104
from Crypto.Util.number import *

cipher = "0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104"

cipher = bytes.fromhex(cipher)

# print(cipher)

# cipher = 0x0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104

# print(long_to_bytes(cipher))

flag_format = b"crypto{"
key = ""

for i in range(7):
    key += chr(flag_format[i] ^ cipher[i])


key = (key + "y").encode()

flag = ""

for i in range(len(cipher)):
    flag += chr(cipher[i] ^ key[i % 8])

print(f"flag = {flag}")


org_key = ""

flag = flag.encode()
for i in range(len(flag)):
    org_key += chr(cipher[i] ^ flag[i])

print(f"org_key = {org_key}")
