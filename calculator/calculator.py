from functions import arithmetic
import utils
from sys import argv, exit
import time

help_msg = """
Usage: python3 run.py [operation] [numbers]

operations: add | subtract | multiply | help
numbers: list of numbers separated by spaces

Example:
>>> python3 calculator.py add 1 2 3 4

Example if using bash script:

>>> ./run.sh add 1 2 3 4
"""

def return_args():
    if len(argv) == 2 and argv[1] == 'help':
        print(help_msg)
        exit()
    elif len(argv) < 4:
        print("Invalid input. Printing help message.")
        print(help_msg)
        exit()
    else:
        operation = argv[1]
        numbers = argv[2:]
        
        return operation, numbers

def main():
    
    operation, numbers = return_args()
    
    print("Operation: ", operation)
    print("Numbers: ", numbers)
    
    valid_operation = utils.validate(numbers)
    
    if valid_operation:
        numbers = utils.floatify(numbers)
        if operation == 'add':
            result = arithmetic.add(numbers)
            print("Result: ", result)
        elif operation == 'subtract':
            result = arithmetic.subtract(numbers)
            print("Result: ", result)
        elif operation == 'multiply':
            result = arithmetic.multiply(numbers)
            print("Result: ", result)
        else:
            print("Invalid operation. Printing help message.")
            print(help_msg)
            exit()
    else:
        print("Invalid operation. Printing help message.")
        print(help_msg)
        exit()
        
if __name__ == '__main__':
    start = time.time_ns()
    main()
    print("Time taken: ", time.time_ns() - start, "ns")