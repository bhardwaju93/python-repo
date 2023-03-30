import functions
import PySimpleGUI as sg


label = sg.Text("Type in a todo")
input_box = sg.InputText(tooltip="Enter todo")
add_button = sg.Button("Add")
list_box = sg.Listbox(values=functions.read_todos(), key='todos',
                      enable_events=True, size=[45, 10])
edit_button = sg.Button("Edit")



window = sg.Window("My To-Do App", layout=[[label], [input_box], [add_button]], font=('Helvetica', 20))

while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todos = functions.read_todos()
            new_todo = values['todo']
            todos.append(new_todo)
            functions.write_lines(todos)

        case "Edit":
            todo = values['todos']

        case sg.WINDOW_CLOSED:
            break


window.close()
