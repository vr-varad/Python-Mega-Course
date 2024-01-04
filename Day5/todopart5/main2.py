while True:
    user_action = input('Type add, show, edit, complete or exit: ').strip()

    if user_action.startswith('add'):
        todo = user_action[4:] + '\n'

        with open('todos.txt', 'r') as file:
            todos = list(file.readlines())

        todos.append(todo)

        with open('todos.txt', 'w+') as filename:
            filename.writelines(todos)

    elif user_action.startswith('show'):

        with open('todos.txt', 'r+') as file:
            todos = file.readlines()

        # new_todos = [x.strip('\n') for x in todos]

        for index, item in enumerate(todos):
            print(f'{index + 1}) {item.capitalize().strip('\n')}')
    elif user_action.startswith('edit'):
        index = int(user_action.partition(" ")[-1])
        todo = input('Enter a new todo: ')

        with open('todos.txt', 'r+') as file:
            todos = list(file.readlines())
            todos[index - 1] = todo + '\n'

        with open('todos.txt', 'w') as file:
            file.writelines(todos)

    elif  user_action.startswith('complete'):
        index = int(user_action.partition(" ")[-1])

        with open('todos.txt', 'r+') as file:
            todos = file.readlines()

        removed_todo = todos.pop(index - 1)

        with open('todos.txt', 'w+') as file:
            file.writelines((todos))

        print(f'Todo {removed_todo.strip('\n').capitalize()} is removed from the todo list.')
    elif user_action.startswith('exit'):
        break
    else:
        print('type a valid string')

print('Bye')
