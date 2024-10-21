def add(arguments):
    value = 0
    for argument in arguments:
        value = value + argument
    return value

def subtract(arguments):
    value = arguments[0]
    minus = arguments[1:]
    for num in minus:
        value = value - num
    return value

def multiply(arguments):
    value = 1
    for argument in arguments:
        value = value * argument
    return value

def divide(arguments):
    value = arguments[0]
    nums = arguments[1:]
    for num in nums:
        value = value / num
    return value