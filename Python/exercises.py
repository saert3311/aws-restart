#Various Python exercises
#I am trying to use python annotations as good practices hehe

def initial() -> None:
    print("Start of exercises")

def welcome_msg(function) -> None:
    print(f'{function.__name__}:')

def exercise1() -> None:
    welcome_msg(exercise1)
    list = ["Ramen", "Hamburger", "Pizza", "Baby Back Ribs", "Sushi"]
    print(f'The 1st item from the list is {list[0]}')
    print(f'The last item from the list is {list[-1]}')

def exercise2(list: list) -> None:
    welcome_msg(exercise2)
    list = [4, 5, 7]
    print(f'Initial list: {list}')
    list.extend([8, 9])
    print(f'Added items list: {list}')
    #for fun lets 
    middle_index = len(list)/2



if __name__ == "__main__":
    initial()
    exercise1()
    exercise2()