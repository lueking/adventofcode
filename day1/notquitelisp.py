def main():
    floor = 0
    pos = 0
    f = open('input.txt')
    for line in f:
        for word in line:
            for char in word:
                pos += 1
                if(char == "("):
                    floor += 1
                if(char == ")"):
                    floor -= 1
                if(floor < 0):
                    print("santa is now in the basement at pos " + str(pos))
                    return

    print("santa is now on floor " + str(floor))

main()


