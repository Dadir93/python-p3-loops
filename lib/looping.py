#!/usr/bin/env python3


def happy_new_year():
    counter = 10
    while counter > 0:
        print(counter)
        counter -= 1
    print("Happy New Year!")

def fizzbuzz_printer():
    for num in range(1, 101):
        print(fizzbuzz(num))

def fizzbuzz():
    for num in range(1, 101):
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)

def reverse_string(string):
    return string[::-1]

def square_integers(int_list):
    return [num ** 2 for num in int_list]

# Test the functions
if __name__ == "__main__":
    happy_new_year()
    fizzbuzz_printer()
    print(reverse_string("Hello, World!"))
    print(square_integers([1, 2, 3, 4, 5]))