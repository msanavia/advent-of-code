#!/usr/bin/env python

input = "input.txt"

with open(input) as file:
    movements = file.read()

    # First year
    x_santa, y_santa = 0, 0
    x_robot, y_robot = 0, 0
    visited_santa = {}
    visited_santa[(x_santa,y_santa)] = visited_santa.get((x_santa,y_santa), 0) + 1

    for move in movements:
        if move == '^':
            x_santa += 1
            visited_santa[(x_santa,y_santa)] = visited_santa.get((x_santa,y_santa), 0) + 1
        elif move == 'v':
            x_santa -= 1
            visited_santa[(x_santa,y_santa)] = visited_santa.get((x_santa,y_santa), 0) + 1
        elif move == '>':
            y_santa += 1
            visited_santa[(x_santa,y_santa)] = visited_santa.get((x_santa,y_santa), 0) + 1
        elif move == '<':
            y_santa -= 1
            visited_santa[(x_santa,y_santa)] = visited_santa.get((x_santa,y_santa), 0) + 1

    # Second year
    x_santa, y_santa = 0, 0
    x_robot, y_robot = 0, 0
    visited_santa_and_robot = {}
    visited_santa_and_robot[(x_robot,y_robot)] = visited_santa_and_robot.get((x_robot,y_robot), 0) + 1
    santa_turn = True

    for move in movements:
        if santa_turn:
            if move == '^':
                x_santa += 1
                visited_santa_and_robot[(x_santa,y_santa)] = visited_santa_and_robot.get((x_santa,y_santa), 0) + 1
            elif move == 'v':
                x_santa -= 1
                visited_santa_and_robot[(x_santa,y_santa)] = visited_santa_and_robot.get((x_santa,y_santa), 0) + 1
            elif move == '>':
                y_santa += 1
                visited_santa_and_robot[(x_santa,y_santa)] = visited_santa_and_robot.get((x_santa,y_santa), 0) + 1
            elif move == '<':
                y_santa -= 1
                visited_santa_and_robot[(x_santa,y_santa)] = visited_santa_and_robot.get((x_santa,y_santa), 0) + 1
            santa_turn = False
        elif not santa_turn:
            if move == '^':
                x_robot += 1
                visited_santa_and_robot[(x_robot,y_robot)] = visited_santa_and_robot.get((x_robot,y_robot), 0) + 1
            elif move == 'v':
                x_robot -= 1
                visited_santa_and_robot[(x_robot,y_robot)] = visited_santa_and_robot.get((x_robot,y_robot), 0) + 1
            elif move == '>':
                y_robot += 1
                visited_santa_and_robot[(x_robot,y_robot)] = visited_santa_and_robot.get((x_robot,y_robot), 0) + 1
            elif move == '<':
                y_robot -= 1
                visited_santa_and_robot[(x_robot,y_robot)] = visited_santa_and_robot.get((x_robot,y_robot), 0) + 1
            santa_turn = True
            
print("Part One's solution: ", len(visited_santa))
print("Part Two's solution: ", len(visited_santa_and_robot))