class NameTooLongError(Exception):
    """ Исключение, которое будет вызвано при передаче в функцию check_name имени длиннее 4 символов """

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"The name '{self.name}' is too long (more than 4 characters)."


def check_name(name):
    """ Проверка имени на длину """
    if len(name) > 4:
        raise NameTooLongError(name)
    else:
        print("Name is valid.")


try:
    check_name("John")  # Валидное имя
    check_name("Jennifer")  # Невалидное имя
except NameTooLongError as e:
    print(e)
