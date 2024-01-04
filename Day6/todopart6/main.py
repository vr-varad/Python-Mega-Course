def get_todos():
    with open('todos.txt', 'r') as file:
        todos = list(file.readlines())
    return todos

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

        todos = get_todos()

        # new_todos = [x.strip('\n') for x in todos]

        for index, item in enumerate(todos):
            print(f'{index + 1}) {item.capitalize().strip('\n')}')
    elif user_action.startswith('edit'):
        try:
            index = int(user_action.partition(" ")[-1])
            todo = input('Enter a new todo: ')

            todos = get_todos()

            todos[index - 1] = todo + '\n'

            with open('todos.txt', 'w') as file:
                file.writelines(todos)
        except "ValueError":
            print('Your command is not valid')
            continue

    elif  user_action.startswith('complete'):
        try:
            index = int(user_action.partition(" ")[-1])

            todos = get_todos()

            removed_todo = todos.pop(index - 1)

            with open('todos.txt', 'w+') as file:
                file.writelines((todos))

            print(f'Todo {removed_todo.strip('\n').capitalize()} is removed from the todo list.')
        except "IndexError":
            print('list index is out of range')
            continue
    elif user_action.startswith('exit'):
        break
    else:
        print('type a valid string')

print('Bye')
