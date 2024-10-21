def validate(numbers):
    allowed_chars = ['.','-']
    digits = ['0','1','2','3','4','5','6','7','8','9']
    for num in numbers:
        chars = list(num)
        not_allowed = [char for char in chars if char not in digits and char not in allowed_chars]
        if len(not_allowed) > 0:
            return False
        elif chars.count('.') > 1:
            return False
        elif chars.count('-') > 1:
            return False
        elif chars.count('-') == 1 and chars.index('-') != 0:
            return False
        else:
            continue
    return True

def floatify(numbers):
    for num in numbers:
        index = numbers.index(num)
        numbers[index] = float(num)
        
    return numbers