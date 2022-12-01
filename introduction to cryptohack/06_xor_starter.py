# For longer binary numbers we XOR bit by bit: 0110 ^ 1010 = 1100.
# We can XOR integers by first converting the integer from decimal to binary.
# We can XOR strings by first converting each character to the integer representing the Unicode character.

# Given the string "label", XOR each character with the integer 13.
# Convert these integers back to a string and submit the flag as crypto{new_string}.

# pwntools xor() function : 물론 도움이 되지만 지금은 xor를 직접 구현해보는게 목표기에 참고만 하자!!

cipher = "label"

flag = ""

for i in cipher:
    flag += chr(ord(i) ^ 13)

print(f"crypto{{{flag}}}")
