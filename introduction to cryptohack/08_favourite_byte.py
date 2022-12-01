# For the next few challenges, you'll use what you've just learned to solve some more XOR puzzles.

# I've hidden some data using XOR with a single byte, but that byte is a secret. Don't forget to decode from hex first.

# 73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d

from Crypto.Util.number import *

cipher = "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"
flag = ""

for i in range(256):
    tempflag = ""
    for b in bytes.fromhex(cipher):
        tempflag += chr(b ^ i)
    if "crypto" in tempflag:
        flag = tempflag
        break

print(flag)
