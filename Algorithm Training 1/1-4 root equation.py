def solution(a, b, c):
    if c < 0:
        return 'NO SOLUTION'
    if a == 0:
        if b == c * c:
            return 'MANY SOLUTIONS'
        return 'NO SOLUTION'
    if c == 0:
        return int(-1 * b / a)
    x1 = int((c * c - b) / a)
    return x1


a = int(input())
b = int(input())
c = int(input())
solutions = solution(a, b, c)
print(solutions)