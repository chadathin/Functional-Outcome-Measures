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

def insertSomething(sql_obj):
    cur = sql_obj.connection.cursor()

    cur.execute("INSERT INTO assessments (unique_ident, name, score) VALUES (%s, %s, %s, %s)",
                ("ABCDE", "QuickDash", 75))

    sql_obj.connection.commit()

    cur.close()
    return 0