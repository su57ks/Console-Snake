from time import time
from random import choice
import keyboard
import threading
import os
import codecs
import json

XSIZE = 15
YSIZE = 13

play_time = time()

with codecs.open("data.json", "r", "utf_8_sig") as f:
    map = json.load(f)["maps"]["default"]

def clear():
    with codecs.open("user.json", "r", "utf_8_sig") as f:
        user = json.load(f)
        if user["enviroment"] == "console":
            os.system('cls' if os.name == 'nt' else 'clear')
        else:
            print("\n" * 100)

def w_move():
    calculate("w")

def a_move():
    calculate("a")

def s_move():
    calculate("s")

def d_move():
    calculate("d")

def close():
    print("Good luck!")
    os._exit(0)

def lst2str(lst):
    string = ""
    for elem in lst:
        string = string + elem + "\n"

    return string[:-1]

def dict2str(dct):
    string = ""
    for i in range(len(dct.keys())):
        string = string + dct[i] + "\n"

    return string[:-1]

def draw(positions_dict):
    positions = positions_dict.values()
    lines = {}
    for y in range(YSIZE):
        line = ""
        for x in range(XSIZE):
            find = False
            for position in positions:
                if position[0] == x and position[1] == y:
                    line += "\033[38;2;255;0;0m██\033[m"
                    find = True
            if find is False:
                color = map["structure"][f"{x}:{y}"]["color"]
                line += f"\033[38;2;{color[0]};{color[1]};{color[2]}m░░\033[m"
        
        lines[y] = line

    print(dict2str(lines))

def out(position):
    if XSIZE > position[0] > -1 and YSIZE > position[1] > -1:
        return position
    if position[0] == -1:
        position[0] = XSIZE - 1
    elif position[0] == XSIZE:
        position[0] = 0

    if position[1] == -1:
        position[1] = YSIZE - 1
    elif position[1] == YSIZE:
        position[1] = 0

    return position

def free(positions_dict):
    positions = list(positions_dict.values())
    free = []
    for y in range(YSIZE):
        for x in range(XSIZE):
            if [x, y] not in positions:
                free.append([x, y])
    return free

def calculate(command):
    global positions
    global hotkey_pressed
    hotkey_pressed.set()
    hotkey_pressed = threading.Event()
    new_positions = {}
    nums = sorted(positions.keys())
    mx = max(nums)
    if command == "w":
        last = [positions[mx][0], positions[mx][1] - 1]
    elif command == "d":
        last = [positions[mx][0] + 1, positions[mx][1]]
    elif command == "s":
        last = [positions[mx][0], positions[mx][1] + 1]
    elif command == "a":
        last = [positions[mx][0] - 1, positions[mx][1]]

    upgr_last = out(last)
    new_positions[mx] = upgr_last

    for num in nums:
        if positions[num] == upgr_last or map["structure"][f"{upgr_last[0]}:{upgr_last[1]}"]["empty"] == False:
            print("You died :(")
            close()
        if num == mx:
            continue
        new_positions[num] = positions[num + 1]

    clear()
        
    draw(new_positions)
    global play_time
    print("Play time:", round(time() - play_time, 2), "seconds")
    positions = new_positions

positions = {-1: [1, 6], 0: [2, 6], 1:[3, 6], 2: [4, 6], 3: [5, 6]}

keyboard.add_hotkey('w', w_move)
keyboard.add_hotkey('a', a_move)
keyboard.add_hotkey('s', s_move)
keyboard.add_hotkey('d', d_move)
keyboard.add_hotkey('ctrl+c', close)

while True:
    hotkey_pressed = threading.Event()

    hotkey_pressed.wait()