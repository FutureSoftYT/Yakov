import random


async def get_cuptcha():
    a = int(random.randint(1, 10))
    b = int(random.randint(1, 10))
    operator = random.choice(['+', '-', '*'])
    res = 0
    if operator == '+':
        res = a + b
    elif operator == '-':
        res = a - b
    elif operator == '*':
        res = a * b
    con = f"{a} {operator} {b}"

    return con,res
