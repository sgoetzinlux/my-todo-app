
def get_todos(filepath="todos.txt"):
    """
Read a text file and return the list of to do items
    :param filepath:
    :param FILEPATH:
    """
    with open("todos.txt", 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath="todos.txt"):
    """
      Write the to do items list in the text file
    :param filepath:
    :param todos_arg:
    :param FILEPATH:
    """
    with open("todos.txt", 'w') as file_local:
        file_local.writelines(todos_arg)
