def area(l, w, h):
    return 2*l*w + 2*w*h + 2*h*l + min([l*w, w*h, h*l])

def parse(line):
    print("Parsing " + str(line))
    bits = []
    pos = 0
    for word in line:
        for char in word:
            if(char == 'x'):
                bits.append(pos)
            pos += 1
    l = line[0:bits[0]]
    w = line[bits[0] + 1: bits[1]]
    h = line[bits[1] + 1:]
    output = {'l': l, 'w': w, 'h': h}
    # print(output)
    return output

def getdata():
    return open('input.txt')

def getRibbonArea(l, w, h):
    dims = [l, w, h]
    dims.pop(dims.index(max(dims)))
    return sum(dims) * 2  + l * w * h

def main():
    data = getdata()
    totalarea = 0
    totalribbon = 0
    for line in data:
        line = line.strip("\n")
        dims = parse(line)
        totalarea += area(int(dims['l']), int(dims['w']), int(dims['h']))
        totalribbon += getRibbonArea(int(dims['l']), int(dims['w']), int(dims['h']))
        print('ribbon length for "' + line + '" is ' + str(getRibbonArea(int(dims['l']), int(dims['w']), int(dims['h']))))

    print('Total paper is ' + str(totalarea) + ' cubic feet.')
    print('Total ribbon length is ' + str(totalribbon) + ' feet.')

main()


