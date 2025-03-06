
shopping_list = {}

def add_item():
    item_name = input("Enter item name: ")
    while True:
        try:
            item_price = int(input("Enter item price: "))
            break
        except ValueError:
            print("Price must be a number")
            continue
    if item_name in shopping_list.keys():
        print("Item already present in shopping list, price will be updated")
    shopping_list[item_name] = item_price
    print(f'Item {item_name} has been added/updated to the shopping list')

def remove_item():
    item_name = input("Enter item name: ")
    if item_name in shopping_list.keys():
        answer = input(f"Do you want to remove {item_name}? (y/n)\n")
        if answer.lower() == 'y':
            shopping_list.pop(item_name)
            print('Item removed')
            return
    print("Item not present in shopping list")

def display_items():
    print('Current shopping list:')
    if len(shopping_list.keys()) == 0:
        print("No items currently present in the shopping list")
        return
    for key, value in shopping_list.items():
        print(f'{key}: {value}')
    print('------------')

def calculate_items_total():
    total = sum(shopping_list.values())
    print(f'Total of items: {total}')


def initial_menu() -> None:
    option = ''
    print('Welcome to the shopping list manager!')
    while True:
        print('What would you like to do?')
        print('(a). Add item')
        print('(b). Remove item')
        print('(c). View list')
        print('(d). Calculate total')
        print('(e). Exit')

        option = input().lower()

        match option:
            case 'a':
                add_item()
            case 'b':
                remove_item()
            case 'c':
                display_items()
            case 'd':
                calculate_items_total()
            case 'e':
                break
            case _:
                print('Invalid option')

    print('Thank you for shopping list!')


if __name__ == '__main__':
    initial_menu()