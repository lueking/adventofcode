def seensay(data):
    lastchar = data[0]
    strlen = 0
    output = ""
    for x in data:
        if x == lastchar:
            strlen += 1
        else:
            output += str(strlen) + lastchar
            strlen = 1
        lastchar = x
    output += str(strlen) + lastchar
    return output

def main():
    data = "3113322113"
    part1 = part2 = data
    for x in range(40):
        part1 = seensay(part1)
    for x in range(50):
        part2 = seensay(part2)
    print(len(part1))
    print(len(part2))

main()