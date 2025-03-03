#Utility functions across all exercises


def initial() -> None:
    '''
    Just an welcome msg at the beginning of exercises
    :return:
    '''
    print("Start of exercises")

def welcome_msg(function) -> None:
    '''
    Prints the function name
    :param function:
    :return:
    '''
    print(f'{function.__name__}:')