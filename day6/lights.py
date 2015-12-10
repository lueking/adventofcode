class Command:
    def __init__(self, term="", start=[], end=[]):
        self.stateChange = term
        self.startDim = start
        self.endDim = end
    def setstatechange(self, statechange):
        self.stateChange = statechange
    def setstartdim(self, startdim):
        self.startDim = startdim
    def setenddim(self, enddim):
        self.endDim = enddim

def parse(line):
    line = line.strip()
    words = line.split(" ")

    command = Command()
    if words[0] == "toggle":
        command.setstatechange(words[0])
    else:
        if words[1] == "on":
            command.setstatechange(words[1])
        elif words[1] == "off":
            command.setstatechange(words[1])
    command.setstartdim(words[-3].split(','))
    command.setenddim(words[-1].split(','))
    return command

def executepart2(command, lightfield):
    lightchange = 0
    if command.stateChange == "on":
        lightchange = 1
    elif command.stateChange == "off":
        lightchange = -1
    elif command.stateChange == "toggle":
        lightchange = 2

    for x in range(int(command.startDim[0]), int(command.endDim[0]) + 1):
        for y in range(int(command.startDim[1]), int(command.endDim[1]) + 1):
            lightfield[x][y] += lightchange
            if lightfield[x][y] < 0:
                lightfield[x][y] = 0
    return lightfield

def executepart1(command, lightfield):
    for x in range(int(command.startDim[0]), int(command.endDim[0]) + 1):
        for y in range(int(command.startDim[1]), int(command.endDim[1]) + 1):
                if command.stateChange == "on":
                    lightfield[x][y] = 1
                elif command.stateChange == "off":
                    lightfield[x][y] = 0
                elif command.stateChange == "toggle":
                    lightfield[x][y] = 0 if lightfield[x][y] == 1 else 1
    return lightfield

def initlist():
    lightfield = [[0 for x in range(1000)] for x in range(1000)]
    return lightfield

def main():
    data = open('input.txt')
    lightfield1 = initlist()
    lightfield2 = initlist()
    for line in data:
        command = parse(line)
        lightfield1 = executepart1(command, lightfield1)
        lightfield2 = executepart2(command, lightfield2)

    count1 = 0
    count2 = 0
    for x in range(1000):
        for y in range(1000):
            if lightfield1[x][y] > 0:
                count1 += 1
            if lightfield2[x][y] > 0:
                count2 += lightfield2[x][y]
    print("There are " + str(count1) + " lights lit")
    print("The total brightness is " + str(count2))

main()