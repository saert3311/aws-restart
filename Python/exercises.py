#Various Python exercises
#I am trying to use python annotations as good practices hehe
from math import floor

def initial() -> None:
    print("Start of exercises")

def welcome_msg(function) -> None:
    print(f'{function.__name__}:')

def exercise1() -> None:
    welcome_msg(exercise1)
    list = ["Ramen", "Hamburger", "Pizza", "Baby Back Ribs", "Sushi"]
    print(f'The 1st item from the list is {list[0]}')
    print(f'The last item from the list is {list[-1]}')

def exercise2() -> None:
    welcome_msg(exercise2)
    list = [4, 5, 7]
    print(f'Initial list: {list}')
    list.extend([8, 9])
    print(f'Added items list: {list}')
    middle_index = floor(len(list)/2)
    list[middle_index] = 99 
    print(f'Modified items list: {list}')

def exercise3():
    welcome_msg(exercise3)
    dict = {
        'Japan':'Tokio',
        'Spain':'Madrid',
        'Venezuela':'Caracas'
    }
    print(f'the capital of Spain is: {dict['Spain']}')

def exercise4():
    welcome_msg(exercise4)
    dict = {
        'name': 'Jose Duarte',
        'age': 40,
        'color':'blue'
    }
    print(f'Current dict: {dict}')
    dict['food'] = 'Ramen'
    print(f'Modified dict: {dict}')

def exercise5():
    welcome_msg(exercise5)
    list = []
    list.append('Orange')
    list.append('Strawberry')
    list.append('Pear')
    list.insert(0, 'Apple')
    print(f'Final list is {list}')

def exercise6():
    welcome_msg(exercise6)
    list = ['Dog', 'Cat', 'Hamster', 'Monkey', 'Pigeon']
    list.remove('Hamster')
    deleted = list.pop()
    print(f'The final list: {list}, and the last removed animal was {deleted}')

if __name__ == "__main__":
    initial()
    exercise1()
    exercise2()
    exercise3()
    exercise4()
    exercise5()
    exercise6()