from utility.utility import *
from random import randint

def exercise1():
    welcome_msg(exercise1)
    fruit_list = ['Pear', 'Apple', 'Orange', 'Banana', 'Strawberry']
    for item in fruit_list:
        print(item)

def exercise2():
    welcome_msg(exercise2)
    your_name = input('What is your name? ')
    for letter in your_name:
        print(letter)

def exercise3():
    welcome_msg(exercise3)
    try:
        while True:
            user_range = int(input('Select a number from 1 to 10: '))
            if user_range not in range(1, 11):
                print('Please select a number from 1 to 10')
                continue
            break
    except ValueError:
        print('Only numbers from are allowed')

    for number in range(1, user_range +1):
        print(f'The square of {number} is {number * number}')

def exercise4():
    welcome_msg(exercise4)
    try:
        while True:
            number = int(input('Select a number: '))
            break
    except ValueError:
        print('Only numbers from are allowed')

    while number != 0:
        print(number)
        number-= 1

def exercise5():
    welcome_msg(exercise5)
    try:
        while True:
            number = int(input('Select a positive number: '))
            if number < 0:
                print('Please select a positive number')
                continue
            print('Thank you!')
            break
    except ValueError:
        print('Only numbers from are allowed')

def exercise6():
    welcome_msg(exercise6)
    while True:
        random_number = randint(1, 10)
        print(f'The random number is {random_number}')
        if random_number == 7: break
        if random_number % 2 == 0:
            continue
        else:
            print(random_number)

if __name__ == '__main__':
    initial()
    exercise1()
    exercise2()
    exercise3()
    exercise4()
    exercise5()
    exercise6()