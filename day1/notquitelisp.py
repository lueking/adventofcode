def main():
    floor = 0
    pos = 0
    count = 0
    for line in open('input.txt'):
        for char in line:
            count += 1
            floor += 1 if char == "(" else -1 if char == ")" else 0
            pos = count if floor < 0 and pos == 0 else pos
    print("santa is now on floor " + str(floor))
    print("Santa hit the basement at pos " + str(pos))
main()