def multiplier(number: int):
    return number * 2


def decorator(func):
    def inner(number):
        if number not in Cash:
            Cash[number] = func(number)
        return Cash[number]
    return inner


multiplier = decorator(multiplier)
Cash = {}
print(multiplier(2))
print(Cash)
print(multiplier(2))
