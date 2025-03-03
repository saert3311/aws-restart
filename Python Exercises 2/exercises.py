from utility.utility import *

def exercise1(val1: int, val2: int) -> None:
    welcome_msg(exercise1)
    print(f'Comparing values: {val1}, {val2}')
    if val1 > val2: print('Greater')
    else:
        print('Less or equal')

def exercise2(compare: str, favorite: str='blue') -> None:
    print('My favorite color!') if compare == favorite else print('Nice color')

def exercise3(condition: str, temp: int) -> None:
    welcome_msg(exercise3)
    if not condition or not temp:
        print('Insuficient data')
        return
    print(f'Conditions are: {condition} and {temp}°C')
    if condition.lower().strip() == 'sunny':
        if temp < 20:
            print('Wear Light jacket')
        else:
            print('Wear T-shirt and shorts')
    elif condition.lower().strip() == 'rainy':
        if temp < 15:
            print('Wear Coat and umbrella')
        else:
            print('Wear Rain jacket')
    else:
        print('Insuficient data')

def exercise4(username: str, password: str) -> None:
    MYUSER = 'jhon'
    MYPASSWORD = 'mypassword'

    welcome_msg(exercise4)
    if not username or not password:
        print('Missing username or password')
        return

    if MYUSER == username:
        if password == MYPASSWORD:
            print('Correct credentials')
        else:
            print('Incorrect password')
    else:
        print('Incorrect username')

def exercise5(age: int, have_membership: str='no') -> None:
    welcome_msg(exercise5)

    is_member = True if have_membership.lower() in ['y', 'yes'] else False
    #if we want to give the best price we have to ask for ages 1st
    #because a member of 8yo wont pay 10 insted of 5
    if age < 12:
        return print('Ticket price is 5$')
    elif age >= 65:
        return print('Ticket price is 8$')
    elif is_member:
        return print('Ticket price is 10$')
    else:
        return print('Ticket price is 15$')

def exercise6() -> None:
    welcome_msg(exercise6)
    while True:
        try:
            price_input = int(input('Input product price:\n'))
            break
        except ValueError:
            print('Product price must be an number')
            continue

    sale_input = input('Product is on Sale: (yes or y)\n')

    is_onsale = True if sale_input.lower() in ['y', 'yes'] else False

    sale_price = price_input - (price_input*0.25) if is_onsale else price_input

    print(f'Original price: {price_input}, Sale price: {sale_price}')

if __name__ == '__main__':
    initial()
    exercise1(9, 7)
    exercise1(5, 7)
    print('Comparing blue')
    exercise2('blue')
    print('Comparing red')
    exercise2('red')
    exercise3('rainy', 20)
    exercise3('rainy', 10)
    exercise3('sunny', 30)
    exercise3('sunny', 15)
    exercise4('jhon', 'mypassword')
    exercise4('jhon', 'another')
    exercise4('may', 'another')
    exercise5(10, 'yes')
    exercise5(77, 'no')
    exercise5(32, 'yes')
    exercise5(21, 'no')
    exercise6()
