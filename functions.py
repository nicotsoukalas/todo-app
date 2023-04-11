FILEPATH = "todos.txt"  # Constant variables are usually with capital letters


def get_todos(filepath=FILEPATH):  # Parameter of the function
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    '''
     default parameter must be placed before the non parameter
     def write_todos(filepath="todos.txt", todos_arg): turn into
     def write_todos(todos_arg, filepath="todos.txt"):
    '''
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)

# print(__name__)
if __name__ == "__main__":
    print("Hello")
    print(get_todos())