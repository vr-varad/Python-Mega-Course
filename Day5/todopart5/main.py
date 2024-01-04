while True:
    user_action = input('Type add, show, edit, complete or exit: ')
    # we can use in operator like add in user_action
    match user_action.partition(" ")[0].strip():
        case 'add':
            todo = user_action.partition(" ")[-1] + '\n'

            with open('todos.txt', 'r') as file:
                todos = list(file.readlines())

            todos.append(todo)

            with open('todos.txt', 'w+') as filename:
                filename.writelines(todos)

        case 'show'|'display':

            with open('todos.txt', 'r+') as file:
                todos = file.readlines()

            # new_todos = [x.strip('\n') for x in todos]

            for index, item in enumerate(todos):
                print(f'{index+1}) {item.capitalize().strip('\n')}')
        case 'edit':
            print('hello')
            index = int(user_action.partition(" ")[-1])
            todo = input('Enter a new todo: ')

            with open('todos.txt', 'r+') as file:
                todos = list(file.readlines())
                todos[index-1] = todo+'\n'

            with open('todos.txt','w') as file:
                file.writelines(todos)

        case 'complete':
            index = int(input('Enter the number of todo you want to mark as completed: '))

            with open('todos.txt','r+') as file:
                todos = file.readlines()

            removed_todo = todos.pop(index-1)

            with open('todos.txt','w+') as file:
                file.writelines((todos))

            print(f'Todo {removed_todo.strip('\n').capitalize()} is removed from the todo list.')
        case 'exit':
            break
        case _:
            print('type a valid string.')

print('Bye')