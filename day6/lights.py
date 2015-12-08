

class Command:
    def __init__(self, term = "", start = [], end = []):
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
    #print("done parsing " + line)
    return command

def execute(command, lightfield):
    for x in range(int(command.startDim[0]), int(command.endDim[0]) + 1):
        for y in range(int(command.startDim[1]), int(command.endDim[1]) + 1):
            if command.stateChange == "on":
                lightfield[x][y] += 1
            elif command.stateChange == "off":
                if lightfield[x][y] > 0:
                    lightfield[x][y] -= 1
            elif command.stateChange == "toggle":
                lightfield[x][y] += 2
    return lightfield

def initlist():
    lightfield = [[0 for x in range(1000)] for x in range(1000)]
    return lightfield

def main():
    data = open('input.txt')
    lightfield = initlist()
    for line in data:
        command = parse(line)
        lightfield = execute(command, lightfield)

    count = 0
    for x in range(1000):
        for y in range(1000):
            count += lightfield[x][y]
            #print("found light on at " + str(x) + ", " + str(y))

    print("The total brightness is " + str(count))

main()