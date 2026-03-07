from time import time
from random import choice

play_time = time()

def draw(positions_dict):
    positions = positions_dict.values()
    lines = {}
    for y in range(13):
        line = ""
        for x in range(15):
            find = False
            for position in positions:
                if position[0] == x and position[1] == y:
                    line += "\033[38;2;255;0;0m██\033[m"
                    find = True
            if find is False:
                line += "\033[38;2;255;255;0m░░\033[m"
        
        lines[y] = line
    for i in range(13):
        print(lines[i])

def out(position):
    if 15 > position[0] > -1 and 13 > position[1] > -1:
        return position
    if position[0] == -1:
        position[0] = 14
    elif position[0] == 15:
        position[0] = 0

    if position[1] == -1:
        position[1] = 12
    elif position[1] == 13:
        position[1] = 0

    return position

def free(positions_dict):
    positions = list(positions_dict.values())
    print(positions)
    free = []
    for y in range(13):
        for x in range(15):
            if [x, y] not in positions:
                free.append([x, y])
    return free

def calculate(positions, command):
    new_positions = {}
    nums = sorted(positions.keys())
    mx = max(nums)
    if command.lower() == "w":
        last = [positions[mx][0], positions[mx][1] - 1]
    elif command.lower() == "d":
        last = [positions[mx][0] + 1, positions[mx][1]]
    elif command.lower() == "s":
        last = [positions[mx][0], positions[mx][1] + 1]
    elif command.lower() == "a":
        last = [positions[mx][0] - 1, positions[mx][1]]

    upgr_last = out(last)
    new_positions[mx] = upgr_last

    for num in nums:
        if positions[num] == upgr_last:
            return "death"
        if num == mx:
            continue
        new_positions[num] = positions[num + 1]
        
    return new_positions

positions = {-1: [1, 6], 0: [2, 6], 1:[3, 6], 2: [4, 6], 3: [5, 6]}
while True:
    print("Play time:", round(time() - play_time, 2), "seconds")

    draw(positions)

    command = input().lower()

    if command == "exit":
        print(":(")
        break
    elif command not in ["w", "a", "s", "d"]:
        print("\n"*100)
        print("unknown command:", command)
        continue

    command = command[0]

    new_positions =  calculate(positions, command)
    if new_positions == "death":
        print("you died(")
        break
    #new_positions[-2] = choice(free(new_positions))
        
    positions = new_positions
    print("\n"*100)