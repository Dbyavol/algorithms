def phone(example, p1, p2, p3):
    example = make_phone(example)
    p1 = make_phone(p1)
    p2 = make_phone(p2)
    p3 = make_phone(p3)
    for x in p1, p2, p3:
        if x == example:
            print("YES")
        else:
            print("NO")


def make_phone(p):
    p = p.replace('-', '').replace('+7', '8').replace('(', '').replace(')', '')
    if len(p) == 7:
        p = '8495' + p
    return int(p)


example = input()
p1 = input()
p2 = input()
p3 = input()
phone(example, p1, p2, p3)