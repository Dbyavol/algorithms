def triangular(a, b, c):
    if a >= b + c:
        return 'No'
    if b >= a + c:
        return 'No'
    if c >= a + b:
        return 'No'
    return 'Yes'


a = int(input())
b = int(input())
c = int(input())
print(triangular(a, b, c))

