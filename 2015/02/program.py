#!/usr/bin/env python

input = "input.txt"
parper_order = 0
ribbon_order = 0

with open(input) as file:
    for line in file:
        l, w, h = map(int, line.split('x')) 
        parper_order += (2 * l * w) + (2 * l * h) + (2 * w * h) + min(l * w, l * h, w * h)
        ribbon_order += min(2 * (l + w), 2 * (l + h), 2 * (w + h)) + (l * w * h)
    print("Part One's solution: ", parper_order)
    print("Part Two's solution: ", ribbon_order)