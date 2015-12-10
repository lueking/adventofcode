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
    return output + str(strlen) + lastchar

def main():
    data = "3113322113"
    for _ in range(40):
        data = seensay(data)
    print(len(data))
    for _ in range(10):
        data = seensay(data)
    print(len(data))

main()