
import functions
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is", now)
while True:
    user_prompt = input("Type add , show , edit , complete or exit:")
    user_prompt = user_prompt.strip()


    if user_prompt.startswith("add"):
        todo = user_prompt[4:]

        todos = functions.read_todos()

        todos.append(todo)

        functions.write_lines(todos)   #todos here goes to todos_local in the defined custom function and todos.txt goes to filepath in the function



    elif user_prompt.startswith("show"):

        todos = functions.read_todos()

        for index, item in enumerate(todos):
            row = f"{index}-{item}"
            item = item.strip('\n')
            print(row)


    elif user_prompt.startswith("edit"):
        try:
            number = int(user_prompt[5:])   # Here we have optimized the code so that instead of asking the user for the input , the program takes it directly from user_prompt
            print(number)
            number = number - 1

            todos = functions.read_todos()
            print("Here is the existing todos:", todos)

            new_todo = input("Enter the new todo:")
            todos[number] = new_todo +'\n'


            print("Here are the new todos:", new_todo)

            functions.write_lines(todos)

        except ValueError:
            print("Invalid Command")
            continue

    elif user_prompt.startswith("complete"):
        try:
            number = int(user_prompt[9:])   # We have used the int function to take input as an integer from the user and then we sliced the input to only take the number

            todos = functions.read_todos()

            index = number -1
            todo_to_remove = todos[index].strip('\n')

            todos.pop(index)

            functions.write_lines(todos)

        except IndexError:
            print("There is no item with that number")


    elif user_prompt.startswith("exit"):

        break


    else:
        print("Invalid Input please try again")

