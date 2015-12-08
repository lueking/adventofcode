import hashlib


def dohash(number, basehash):
    basehash.update(number.encode())
    return basehash.hexdigest()


def main():
    base = "ckczppom".encode()
    basehash = hashlib.md5()
    basehash.update(base)
    output = ""
    number = 0
    while output[:7] != "0000000":
        number += 1
        copy = basehash.copy()
        output = dohash(str(number), copy)
        if number % 100000 == 0:
            print('computed ' + str(output) + " from " + str(base) + " and " + str(number))
    print("found goal: " + str(output) + " from " + str(base) + " and " + str(number))

main()
