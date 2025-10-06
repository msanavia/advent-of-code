#!/usr/bin/env python

import re

input = "input.txt"

def get_coords(string):
    coords = re.findall(r"(\d+),(\d+)", string)
    start_coords = (int(coords[0][0]), int(coords[0][1]))
    end_coords = (int(coords[1][0]), int(coords[1][1]))
    return start_coords, end_coords

def get_action(string):
    if len(re.findall(r"turn on", string)) > 0: return "ON"
    if len(re.findall(r"turn off", string)) > 0: return "OFF"
    if len(re.findall(r"toggle", string)) > 0: return "TOGGLE"

lenght = 1000
grid_1 = [[False for x in range(lenght)] for y in range(lenght)]
grid_2 = [[0 for x in range(lenght)] for y in range(lenght)]
lights_on = 0
brightness = 0

with open(input) as file:
    for line in file:
        start, end = get_coords(line)
        for y in range(start[1], end[1] + 1):
            for x in range(start[0], end[0] + 1):
                if get_action(line) == "ON":
                    if not grid_1[x][y]: lights_on += 1
                    grid_1[x][y] = True
                    grid_2[x][y] += 1
                    brightness += 1
                if get_action(line) == "OFF":
                    if grid_1[x][y]: lights_on -= 1
                    grid_1[x][y] = False
                    if grid_2[x][y] > 0:
                        grid_2[x][y] -= 1
                        brightness -= 1
                if get_action(line) == "TOGGLE":
                    if grid_1[x][y]: lights_on -= 1
                    else: lights_on += 1
                    grid_1[x][y] = not grid_1[x][y]
                    grid_2[x][y] += 2
                    brightness += 2

    print("Part One's solution: ", lights_on)
    print("Part Two's solution: ", brightness)