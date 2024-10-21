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