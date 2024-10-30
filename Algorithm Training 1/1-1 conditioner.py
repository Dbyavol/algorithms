def conditioner(room, purpose, cond_type):
    if cond_type == 'freeze':
        if purpose < room:
            return purpose
        return room
    if cond_type == 'heat':
        if purpose > room:
            return purpose
        return room
    if cond_type == 'auto':
        return purpose
    if cond_type == 'fan':
        return room


room, cond = map(int, input().split(' '))
typ = input()
print(conditioner(room, cond, typ))