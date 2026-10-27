import re, random

CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
VOWELS = 'aeiouy'

def check(regex, name):
    match = re.search(regex, name)
    if match: return match.group(0) == name
    return False

def replaceRandom(t, a, b):
    l = [i for i, char in enumerate(t) if char == a]
    if not l: return t
    t = list(t)
    t[random.choice(l)] = b
    return ''.join(t)

def generateName(rules):
    o = rules[0]*random.randint(1, 4)
    if rules[1]:
        for i in rules[1]:
            if i in CONSONANTS: o = replaceRandom(o, 'C', i)
            elif i in VOWELS: o = replaceRandom(o, 'V', i)
    o = list(o)
    for i in range(len(o)):
        if o[i] == 'C': o[i] = random.choice(CONSONANTS)
        elif o[i] == 'V': o[i] = random.choice(CONSONANTS)
    return ''.join(o)

def perturb(rules, level):
    return rules # implement later

def generateQueue(rules, level):
    o = []
    for i in range(random.randint(max(int(level*0.75), 1), max(int(level*1.25), level+1))):
        if random.randint(0, max(level//2, 1)): o.append(generateName(rules))
        else: o.append(generateName(perturb(rules, level)))
    return o

for i in range(10):
    print(generateQueue(['CVC', 'abcd'], i+1))
