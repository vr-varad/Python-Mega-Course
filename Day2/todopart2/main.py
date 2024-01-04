todos = []

while True:
    user_action = input('Type add, show or exit: ').strip()
    match user_action:
        case 'add':
            todo = input('Enter a todo: ')
            todos.append(todo)
        case 'show'|'display':
            for index, item in enumerate(todos):
                print(f'{index+1}) {item.title()}')
        case 'edit':
            index = int(input('Enter the number of todo to edit: '))
            todo = input('Enter a new todo: ')
            todos[index-1] = todo
        case 'exit':
            break
        case _:
            print('type a valid string.')

print('Bye')