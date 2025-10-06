#!/usr/bin/env python

input = "input.txt"
floor = 0
counter = 0
in_basement = False

with open(input) as file:
    for char in file.read():
        counter += 1
        floor +=1 if char == '(' else -1
        if floor < 0 and not in_basement:
            in_basement = True
            print(f"Part Two's solution: {counter}")
        
print("Part One's solution: ", floor)
