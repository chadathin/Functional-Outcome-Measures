from random import choice

def makeSelect():
    out = ''
    alphaNum = 'ABCDEFGHJKMNPQRSTUVWXYZ23456789'
    for _ in range(50):
        out += choice(alphaNum)
    return out


def randString():
    select = makeSelect()
    out = ''
    for _ in range(8):
        out+=choice(select)
    return out