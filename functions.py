FILEPATH = "todos.txt"                        #Declaring a variable for file path so that in future we are wiring more complex code and we need to change the file in which we are storing our data we only have to change it once.

def read_todos(filepath=FILEPATH):
    """
   Read a text file and return the list of to-do items.
    """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local

def write_lines(todos_local ,filepath=FILEPATH):
    with open('todos.txt', 'w') as file_loc:
        file_loc.writelines(todos_local)


if __name__ == "__Day13__":                    #We are using if name and then in equals to we need write the name of the main python code file and we use this in case we don't want this code block to run with the main file code
    print("Hello World from Functions")
