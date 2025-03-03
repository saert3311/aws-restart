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