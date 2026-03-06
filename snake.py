def draw(positions_dict):
    print("\n"*100)
    print(positions_dict)
    positions = positions_dict.values()
    lines = {}
    for y in range(13):
        #print("console", y)
        line = ""
        #print(" ", line)
        for x in range(15):
            #print("~console", x)
            find = False
            for position in positions:
                #print("~#console", position)
                if position[0] == x and position[1] == y:
                    line += "██"
                    find = True
            if find is False:
                line += "░░"
                #print("~#console", line)
        
        lines[y] = line
        #print("console", lines)
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
        if num == mx:
            continue
        new_positions[num] = positions[num + 1]
        
    return new_positions

positions = {-1: [0, 1], 0: [1, 1], 1:[2, 1], 2: [3, 1]}
while True:
    draw(positions)

    command = input()

    if command == "exit":
        break

    new_positions =  calculate(positions, command)
    positions = new_positions