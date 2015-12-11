def isnaughty(line):
    for bad in ["ab", "cd", "pq", "xy"]:
        if line.count(bad) > 0:
            return True
    return False

def hasdubs(line):
    lastchar = ""
    for char in line:
        if char == lastchar:
            return True
        lastchar = char
    return False

def hasvowels(line):
    vowels = 0
    for char in line:
        vowels += 1 if char in ["a", "e", "i", "o", "u"] else 0
    return True if  vowels >= 3 else False

def main():
    data = open('input.txt')
    nice = 0
    total = 0
    for line in data:
        line = line.strip()
        total += 1
        nice += 1 if not isnaughty(line) and hasdubs(line) and hasvowels(line) else 0
    print(nice)


main()
