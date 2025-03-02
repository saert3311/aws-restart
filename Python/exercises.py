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

def exercise3() -> None:
    welcome_msg(exercise3)
    dict = {
        'Japan':'Tokio',
        'Spain':'Madrid',
        'Venezuela':'Caracas'
    }
    print(f'the capital of Spain is: {dict['Spain']}')

def exercise4() -> None:
    welcome_msg(exercise4)
    dict = {
        'name': 'Jose Duarte',
        'age': 40,
        'color':'blue'
    }
    print(f'Current dict: {dict}')
    dict['food'] = 'Ramen'
    print(f'Modified dict: {dict}')

def exercise5() -> None:
    welcome_msg(exercise5)
    list = []
    list.append('Orange')
    list.append('Strawberry')
    list.append('Pear')
    list.insert(0, 'Apple')
    print(f'Final list is {list}')

def exercise6() -> None:
    welcome_msg(exercise6)
    list = ['Dog', 'Cat', 'Hamster', 'Monkey', 'Pigeon']
    list.remove('Hamster')
    deleted = list.pop()
    print(f'The final list: {list}, and the last removed animal was {deleted}')

def exercise7() -> None:
    welcome_msg(exercise7)
    list = [3, 5, 1, 4, 9]
    print(f'Original list: {list}')
    list.sort()
    print(f'Sorted List: {list}')
    list.reverse()
    print(f'Reversed List: {list}')

def exercise8() -> None:
    welcome_msg(exercise8)
    dict = {
        'Lord of the Rings': 'J.R.R. Tolkien',
        'Hunger Games': 'Suzanne Collins',
        'Da Vinci code': 'Dan Brown'
    }
    print(f'The author from Lords of the rings is: {dict.get('Lord of the Rings', 'Unknown')}')
    print(f'The author from Twilight is: {dict.get('Twilight', 'Unknown')}')

def exercise9() -> None:
    welcome_msg(exercise9)
    dict = {
        'Jhon': 4,
        'Diana': 7,
        'Amy': 2,
        'Tommy': 6,
        'Alicia': 10
    }

    print(f'Classroom subjects: {dict.keys()}')
    print(f'Classroom numbers: {dict.values()}')

def exercise10() -> None:
    welcome_msg(exercise10)
    dict1 = {
        'Jhon': 4.1,
        'Mary': 5.7,
        'Maria': 8.2
    }
    dict2 = {
        'Lorraine': 4.5,
        'Danny': 5.9,
        'Sophia': 9.3
    }

    dict1.update(dict2)
    print(f'Combined dict is: {dict1}')

def exercise11() -> None:
    welcome_msg(exercise11)
    selected_numbers = []
    while len(selected_numbers) < 10:
        try:
            number = int(input(f'Input a number from 1 to 100: ({len(selected_numbers)+1} of 10) \n'))
            if number < 1 or number > 100:
                print('Number must be between 1 to 100')
                continue
            selected_numbers.append(number)
        except ValueError: #we capture if the int cant convert to numbers
            print('Only whole numbers are accepted')
    big_numbers = [number for number in selected_numbers if number > 50]
    #i love list and dict comprehensions hehe
    avg = sum(big_numbers) / len(big_numbers)
    big_numbers.append(avg)
    print(f'Normal list: {selected_numbers}')
    print(f'Big number list: {big_numbers}')
    print(f'Average: {avg}')


def exercise12():
    welcome_msg(exercise12)

    def get_number_input(msg: str, min :int=2) -> int:
        while True:
            try:
                number = int(input(f'{msg}\n'))
                if number < min:
                    print('Value must be a minimun of {min}')
                    continue
                return number
            except ValueError:
                print('Only numbers are accepted')

    data_dict = {}
    number_departments = get_number_input('How many departments?')

    #now filling department names
    while len(data_dict) < number_departments:
        department_name = input(f'Give a name for department: {len(data_dict)+1} of { number_departments}\n')
        data_dict[department_name] = []
    for department in data_dict.keys():
        n_employees = get_number_input(f'How many employees for {department}?')
        while len(data_dict[department]) < n_employees:
            name = input(f'Name of employee: ({len(data_dict[department])+1} of {n_employees})\n')
            salary = int(input(f'Salary of employee: ({len(data_dict[department])+1} of {n_employees})\n'))
            data_dict[department].append((name, salary))

    highest_paid = ('', 0) #we initialize in zero to not mess with comparison and to keep afterwards
    for (department, data) in data_dict.items():
        sum_department = sum([int(data[1]) for data in data]) #list comphension yay
        print(f'The department of: {department} has a total of {sum_department}')
        highest_paid = max([highest_paid] + data, key=lambda element: element[1])
        #So instead of comparing everyone it will be more memory intensive
        #lets use the max from current department and top from previous
        #at the end of the cycle we already have the max hehe
    print(f'The highest paid employee across all departments is {highest_paid[0]}')


if __name__ == "__main__":
    initial()
    exercise1()
    exercise2()
    exercise3()
    exercise4()
    exercise5()
    exercise6()
    exercise7()
    exercise8()
    exercise9()
    exercise10()
    exercise11()
    exercise12()