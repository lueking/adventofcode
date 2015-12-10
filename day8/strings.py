totallength = 0
modlength = 0
genlen = 0
for line in open("input3.txt").read().split("\n"):
    length = len(line)
    totallength += length
    for x in ["\"", "\\"]:
        genlen += line.count(x)
    for x in ["\\\\", '\\"',"\\x"]:
        length -= line.count(x, 1, -1) * (3 if x == "\\x" else 1)
        line = line.replace(x, "+") if x != "\\x" else line
    genlen += 2
    modlength += length - 2
print(totallength - modlength)
print(genlen)