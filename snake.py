from time import time
from random import choice
import keyboard
import threading
import os
import codecs
import json

class Snake():
    def __init__(self, pName = "User"):
        with codecs.open("data.json", "r", "utf_8_sig") as f:
            self.map = json.load(f)["maps"]["default"]
        self.name = pName
        self.apple = []
        self.score = 0
        self.binded = {}
        self.XSIZE = self.map["size"][0]
        self.YSIZE = self.map["size"][1]
        self.play_time = time()
        self.start = self.map["start"]
        self.positions = {}
        self.hotkey_pressed = threading.Event()
        self.running = True
        for key in self.start:
            self.positions[int(key)] = self.start[key]
        keyboard.add_hotkey('w', self.w_move)
        keyboard.add_hotkey('a', self.a_move)
        keyboard.add_hotkey('s', self.s_move)
        keyboard.add_hotkey('d', self.d_move)
        keyboard.add_hotkey('ctrl+c', self.close)

    def run(self):
        self.draw()
        while self.running:
            self.hotkey_pressed.wait()

    def clear(self):
        with codecs.open("user.json", "r", "utf_8_sig") as f:
            user = json.load(f)
            if user["environment"] == "console":
                os.system('cls' if os.name == 'nt' else 'clear')
            else:
                print("\n" * 100)

    def keyByValue(self, dct, value):
        for key in dct.keys():
            if dct[key] == value:
                return key

    def w_move(self):
        self.calculate("w")

    def a_move(self):
        self.calculate("a")

    def s_move(self):
        self.calculate("s")

    def d_move(self):
        self.calculate("d")

    def close(self):
        print("Good luck!")
        keyboard.unhook_all()
        os._exit(0)

    def lst2str(self, lst):
        string = ""
        for elem in lst:
            string = string + elem + "\n"

        return string[:-1]

    def dict2str(self, dct):
        string = ""
        for i in range(len(dct.keys())):
            string = string + dct[i] + "\n"

        return string[:-1]

    def draw(self):
        print(self.positions)
        positions = self.positions.values()
        lines = {}
        for y in range(self.YSIZE):
            line = ""
            for x in range(self.XSIZE):
                find = False
                for position in positions:
                    key = self.keyByValue(self.positions, position)
                    if position == [x, y] and key != -1:
                        line += "\033[38;2;255;0;0m██\033[m"
                        find = True
                if find is False:
                    if [x, y] == self.apple:
                        line += "\033[38;2;0;255;0m██\033[m"
                    else:
                        color = self.map["structure"][f"{x}:{y}"]["color"]
                        line += f"\033[38;2;{color[0]};{color[1]};{color[2]}m░░\033[m"
            
            lines[y] = line

        print(self.dict2str(lines))

    def out(self, position):
        if self.XSIZE > position[0] > -1 and self.YSIZE > position[1] > -1:
            return position
        if position[0] == -1:
            position[0] = self.XSIZE - 1
        elif position[0] == self.XSIZE:
            position[0] = 0

        if position[1] == -1:
            position[1] = self.YSIZE - 1
        elif position[1] == self.YSIZE:
            position[1] = 0

        return position

    def free(self, head):
        positions = list(self.positions.values())
        free = []
        near = [self.out([head[0] + 1, head[1]]), self.out([head[0] - 1, head[1]]), self.out([head[0], head[1] + 1]), self.out([head[0], head[1] - 1]), ]
        for y in range(self.YSIZE):
            for x in range(self.XSIZE):
                if [x, y] not in positions and self.map["structure"][f"{x}:{y}"]["empty"] == True and [x, y] not in near:
                    free.append([x, y])
        return free

    def calculate(self, command):
        self.hotkey_pressed.set()
        new_positions = {}
        nums = sorted(self.positions.keys())
        mx = max(nums)
        if command == "w":
            last = [self.positions[mx][0], self.positions[mx][1] - 1]
        elif command == "d":
            last = [self.positions[mx][0] + 1, self.positions[mx][1]]
        elif command == "s":
            last = [self.positions[mx][0], self.positions[mx][1] + 1]
        elif command == "a":
            last = [self.positions[mx][0] - 1, self.positions[mx][1]]

        upgr_last = self.out(last)

        if self.map["structure"][f"{upgr_last[0]}:{upgr_last[1]}"]["empty"] == False:
                print("You died :(")
                self.close()

        for num in nums:
            if self.positions[num] == upgr_last:
                print("You died :(")
                self.close()

        if upgr_last == self.apple:
            self.score += 1
            self.apple = []
            new_positions[mx + 1] = upgr_last
            for num in nums:
                if num == mx:
                    continue
                new_positions[num + 1] = self.positions[num + 1]
            new_positions[-1] = self.positions[-1]
        else:
            new_positions[mx] = upgr_last

            for num in nums:
                if num == mx:
                    continue
                new_positions[num] = self.positions[num + 1]

        self.clear()
        if self.apple == []:
            free_ = self.free(upgr_last)
            self.apple = choice(free_)
        self.draw()
        global play_time
        print("Play time:", round(time() - self.play_time, 2), "seconds")
        print("Score:", self.score)
        self.positions = new_positions

snake = Snake()
snake.run()