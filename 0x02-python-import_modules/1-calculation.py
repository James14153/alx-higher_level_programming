#!/usr/bin/python3

import calculator_1
    
a = 10
b = 5

def main():
    sum = calculator_1.add(a, b)
    print ("{} + {} = {}".format(a, b, sum))
    
    differrence = calculator_1.sub(a, b)
    print ("{} - {} = {}".format(a, b, differrence))
    
    multiplication = calculator_1.mul(a, b)
    print ("{} * {} = {}".format(a, b, multiplication))
    
    division = calculator_1.div(a, b)
    print ("{} / {} = {}".format(a, b, division))

if __name__ == "__main__":
    main()

