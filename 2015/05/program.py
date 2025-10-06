#!/usr/bin/env python

import re

input = "input.txt"

vowels = ["a", "e", "i", "o", "u"]
bad_couples = ["ab", "cd", "pq", "xy"]
nice_strings_count_1 = 0
nice_strings_count_2 = 0

def is_nice_1(string):
    vowels_count = 0
    bad_couples_count = 0
    repeated_letter_1 = False
    for vowel in vowels:
        if string.count(vowel) > 0: vowels_count += string.count(vowel)
    for couple in bad_couples:
        if string.count(couple) > 0: bad_couples_count += string.count(couple)
    for letter in string:
        if string.count(letter+letter) >= 1: repeated_letter_1 = True
    return True if vowels_count >= 3 and bad_couples_count <= 0 and repeated_letter_1 else False
    
def is_nice_2(string):
    double_pair = re.findall(r"(..).*\1", string)
    repeated_letter_2 = re.findall(r"(.).\1", string)
    return True if len(double_pair) > 0 and len(repeated_letter_2) > 0  else False

with open(input) as file:
    for line in file:
        if is_nice_1(line):
            nice_strings_count_1 += 1
        if is_nice_2(line):
            nice_strings_count_2 += 1
print("Part One's solution: ", nice_strings_count_1)
print("Part Two's solution: ", nice_strings_count_2)
