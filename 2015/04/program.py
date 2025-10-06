#!/usr/bin/env python

import hashlib

input = "yzbqklnj"
index = 0

while not hashlib.md5((input+str(index)).encode()).hexdigest().startswith('00000'):
    index += 1
print(f"Part One's solution: {index} ({hashlib.md5((input+str(index)).encode()).hexdigest()})")

index = 0
while not hashlib.md5((input+str(index)).encode()).hexdigest().startswith('000000'):
    index += 1
print(f"Part Two's solution: {index} ({hashlib.md5((input+str(index)).encode()).hexdigest()})")