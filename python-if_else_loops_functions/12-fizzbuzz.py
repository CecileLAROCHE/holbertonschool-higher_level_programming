#!/usr/bin/python3

def fizzbuzz():
    for code in range(1, 101):
        if code % 15 == 0:
            print("FizzBuzz", end=' ')
        elif code % 3 == 0:
            print("Fizz", end=' ')
        elif code % 5 == 0:
            print("Buzz", end=' ')
        else:
            print(code, end=' ')
