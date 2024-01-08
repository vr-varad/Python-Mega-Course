import functions
import PySimpleGUI as sg
import time

sg.theme('Black')
clock = sg.Text('', key='clock')
label = sg.Text("Type in a to-do: ")
input_box = sg.InputText(tooltip="Enter The todo", key='todo')
list_box = sg.Listbox(values=functions.get_todos(),key='todos',enable_events=True,size=[45,10])

add_button = sg.Button('Add')
edit_button = sg.Button('Edit')
complete_button = sg.Button('Complete')
exit_button = sg.Button('Exit')

window = sg.Window("My To-Do App",
                   layout=[[clock],[label], [input_box, add_button],[list_box,edit_button,complete_button], [exit_button]],
                   font=('Helvetica', 20))
while True:
    event, values = window.read(timeout=10)
    window['clock'].update(value=f"Today's todo: {time.strftime('%H:%M:%S, %d %b %Y')}")
    match event:
        case "Add":
            todos = functions.get_todos()
            todos.append(values['todo'].capitalize() + '\n')
            functions.write_todo(todos)
            window['todo'].update(value='')
            window['todos'].update(values=todos)
        case "Edit":
            try:
                todos = functions.get_todos()
                todos[todos.index(values['todos'][0])] = values['todo']
                functions.write_todo(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value='')
            except IndexError:
                sg.popup('Select Something to Edit',font=('Helvetica', 20))

        case 'Complete':
            try:
                todos = functions.get_todos()
                todos.pop(todos.index(values['todos'][0]))
                functions.write_todo(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value='')
            except IndexError:
                sg.popup('Select Something to Complete',font=('Helvetica', 20))
        case 'todos':
            window['todo'].update(value=values['todos'][0])
        case 'Exit' | sg.WIN_CLOSED:
            break
window.close()
