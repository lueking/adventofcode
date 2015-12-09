class gives():
    def __init__(self, left, right):
        self.left = left
        self.right = right
    def execute(self):
        #print(self)
        vals[self.right.value] = num(self.left.execute())
        return vals[self.right.value].execute()
    def __str__(self):
        return str(self.left) + " -> " + str(self.right)

class orgate():
    def __init__(self, left, right):
        self.left = left
        self.right = right
    def execute(self):
        return self.left.execute() | self.right.execute()
    def __str__(self):
        return str(self.left) + " OR " + str(self.right)

class andgate():
    def __init__(self, left, right):
        self.left = left
        self.right = right
    def execute(self):
        return self.left.execute() & self.right.execute()
    def __str__(self):
        return str(self.left) + " AND " + str(self.right)

class notgate():
    def __init__(self, right):
        self.right = right
    def execute(self):
        return ~ self.right.execute()
    def __str__(self):
        return "NOT " + str(self.right)

class lshift():
    def __init__(self, left, right):
        self.left = left
        self.right = right
    def execute(self):
        return self.left.execute() << self.right.execute()
    def __str__(self):
        return str(self.left) + " LSHIFT " + str(self.right)

class rshift():
    def __init__(self, left, right):
        self.left = left
        self.right = right
    def execute(self):
        return self.left.execute() >> self.right.execute()
    def __str__(self):
        return str(self.left) + " RSHIFT " + str(self.right)

class var():
    def __init__(self, value):
        if value not in vals.keys():
            vals[value] = 0
        self.value = value
    def execute(self):
        if type(vals.get(self.value)) is int:
            return vals.get(self.value)
        return vals.get(self.value).execute()
    def __str__(self):
        return str(self.value)

class num():
    def __init__(self, value):
        self.value = int(value)
    def execute(self):
        return self.value
    def __str__(self):
        return str(self.value)

def makeleaf(leaf):
    if leaf.isdecimal():
        return num(leaf)
    else:
        return var(leaf)

def parse(line):
    givesTerms = line.split(' -> ')

    if 'NOT' in givesTerms[0]:
        left = notgate(makeleaf(givesTerms[0].split('NOT ')[1]))
    elif 'AND' in givesTerms[0]:
        leftnode = makeleaf(givesTerms[0].split(' AND ')[0])
        rightnode = makeleaf(givesTerms[0].split(' AND ')[1])

        left = andgate(leftnode, rightnode)
    elif 'OR' in givesTerms[0]:
        leftnode = makeleaf(givesTerms[0].split(' OR ')[0])
        rightnode = makeleaf(givesTerms[0].split(' OR ')[1])

        left = orgate(leftnode, rightnode)
    elif 'RSHIFT' in givesTerms[0]:
        leftnode = makeleaf(givesTerms[0].split(' RSHIFT ')[0])
        rightnode = makeleaf(givesTerms[0].split(' RSHIFT ')[1])

        left = rshift(leftnode, rightnode)
    elif 'LSHIFT' in givesTerms[0]:
        leftnode = makeleaf(givesTerms[0].split(' LSHIFT ')[0])
        rightnode = makeleaf(givesTerms[0].split(' LSHIFT ')[1])

        left = lshift(leftnode, rightnode)
    else:
        left = makeleaf(givesTerms[0].strip())

    right = makeleaf(givesTerms[1].strip())

    vals[right.value] = gives(left, right)
    return right.value

vals = {}

def main():
    global vals
    data = open('input.txt')
    for line in data:
        key = parse(line.strip())
        #print("setting: '" + key + "' to " + str(vals.get(key).left))
    data.close()
    print("Finding out the vaue of wire 'a': " + str(vals['a'].execute()))
    print("Setting wire 'b' to that value.")

    vals = {}
    data = open('input.txt')
    for line in data:
        key = parse(line.strip())
        #print("setting: '" + key + "' to " + str(vals.get(key).left))
    data.close()

    gives(num(16076), var('b')).execute()
    print("The new value of wire 'a' is: " + str(vals['a'].execute()))

main()