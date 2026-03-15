from time import time
from random import choice
import keyboard
import threading
import os
import codecs
import json

with codecs.open("data.json", "r", "utf_8_sig") as f:
    map = json.load(f)["maps"]["default"]

XSIZE = map["size"][0]
YSIZE = map["size"][1]

apple = []

score = 0

play_time = time()

def clear():
    with codecs.open("user.json", "r", "utf_8_sig") as f:
        user = json.load(f)
        if user["enviroment"] == "console":
            os.system('cls' if os.name == 'nt' else 'clear')
        else:
            print("\n" * 100)

def keyByValue(dct, value):
    for key in dct.keys():
        if dct[key] == value:
            return key

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
    keyboard.unhook_all()
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
                key = keyByValue(positions_dict, position)
                if position == [x, y] and key != -1:
                    line += "\033[38;2;255;0;0m██\033[m"
                    find = True
            if find is False:
                global apple
                if [x, y] == apple:
                    line += "\033[38;2;0;255;0m██\033[m"
                else:
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

def free(positions_dict, head):
    positions = list(positions_dict.values())
    free = []
    near = [out([head[0] + 1, head[1]]), out([head[0] - 1, head[1]]), out([head[0], head[1] + 1]), out([head[0], head[1] - 1]), ]
    for y in range(YSIZE):
        for x in range(XSIZE):
            if [x, y] not in positions and map["structure"][f"{x}:{y}"]["empty"] == True and [x, y] not in near:
                free.append([x, y])
    return free

def calculate(command):
    global positions
    global hotkey_pressed
    global score
    global apple
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
    if upgr_last == apple:
        score += 1
        apple = []
    new_positions[mx] = upgr_last

    for num in nums:
        if positions[num] == upgr_last or map["structure"][f"{upgr_last[0]}:{upgr_last[1]}"]["empty"] == False:
            print("You died :(")
            close()
        if num == mx:
            continue
        new_positions[num] = positions[num + 1]

    clear()
    if apple == []:
        free_ = free(new_positions, upgr_last)
        apple = choice(free_)
    draw(new_positions)
    global play_time
    print("Play time:", round(time() - play_time, 2), "seconds")
    print("Score:", score)
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