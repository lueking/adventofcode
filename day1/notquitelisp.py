def main():
    floor = 0
    pos = 0
    count = 0
    for line in open('input.txt'):
        for word in line:
            for char in word:
                count += 1
                floor += 1 if(char == "(") else -1
                if floor < 0 and not pos == 0:
                    print("santa is now in the basement at pos " + str(pos))
                    pos = count
    print("santa is now on floor " + str(floor))
    print("Santa hit the basement at pos " + str(pos))
main()


