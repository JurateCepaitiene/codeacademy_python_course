import math

def sum (*args):
    total = 0
    for x in args:
        total += x
    return total

print(sum(2,5,6))

def square_root(x: float) -> float:
    answer = math.sqrt(x)
    return answer

print(square_root(9.0))
