#from functions import get_todos, write_todos
import functions # Local module
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is", now)
while True:
    user_action = input("Type add, show, edit, complete or exit:  ")
    user_action = user_action.strip()

    if user_action.startswith("add") :
        todo = user_action[4:]  # slicing lists  [n : n] ==  [>n : <n]
        # todo = input("Enter a todo: ") + "\n"  merge a break line in the string

        ''' 
            file = open('todos.txt', 'r') # open the file
            todos = file.readlines() # read opened file and store in todos var
            file.close() 
        '''

        todos = functions.get_todos()  # Argument of the function
        todos.append(todo + "\n")

        functions.write_todos(todos)

    elif user_action.startswith("show"):  # remember to include the display option in the future

        todos = functions.get_todos()

        ''' new_todos = []
        for item in todos:
           new_item = item.strip("\n")  # removes the \n from each item in the list
           new_todos.append(new_item)

        new_todos = [item.strip("\n") for item in todos]  # list comprehension -
        does the same as the block of code above - You don't need to declare the variable
        '''
        for index, item in enumerate(todos):
            item = item.strip('\n') # Instead of removing with list comprehension
            row = f"{index + 1}-{item}"
            print(row)
    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            number = number - 1

            todos = functions.get_todos()

            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + "\n"

            functions.write_todos(todos)
        except ValueError:
            print("Your command is not valid!")
            continue

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])

            todos = functions.get_todos()

            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            functions.write_todos(todos)


            message = f"Todo {todo_to_remove} was removed from te list."
            print(message)
        except IndexError:
            print("There is no item with that number.")
            continue
    elif user_action.startswith("exit"):
        break
        # case _:
        # print("Hey, You entered an unknown command!")

    else:
        print("Command is not valid!")

print("Bye!")
