while True:
    user_action = input('Type add, show, edit, complete or exit: ').strip()
    match user_action:
        case 'add':
            todo = input('Enter a todo: ') + '\n'
            file = open('todos.txt', 'r')
            todos = list(file.readlines())
            file.close()
            todos.append(todo)
            filename = open('todos.txt', 'w+')
            filename.writelines(todos)
            filename.close()
        case 'show'|'display':
            file = open('todos.txt','r')
            todos = file.readlines()
            for index, item in enumerate(todos):
                print(f'{index+1}) {item.title().replace('\n','')}')
        case 'edit':
            index = int(input('Enter the number of todo to edit: '))
            todo = input('Enter a new todo: ')
            todos[index-1] = todo
        case 'complete':
            index = int(input('Enter the number of todo you want to mark as completed: '))
            todos.pop(index-1)
        case 'exit':
            break
        case _:
            print('type a valid string.')

print('Bye')