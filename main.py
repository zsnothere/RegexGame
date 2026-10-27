import re

def check(regex, name):
    match = re.search(regex, name)
    if match: return match.group(0) == name
    return False

def generateName(rules):
    o = ''
    for i in rules[0]:
        if i == 'C':
            o += 'bcdfghjklmnpqrstvwxyz'[random.randint(0,20)]
        else:
            o += 'aeiouy'[random.randint(0,5)]
    return o
