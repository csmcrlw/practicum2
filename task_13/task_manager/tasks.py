# Модуль tasks.py
tasks = []


def add_task():
    """ Метод для добавления новой задачи """

    task = input("Введите новую задачу: ")
    tasks.append(task)
    print("Задача добавлена успешно.")


def view_tasks():
    """ Метод для просмотра списка задач """

    if tasks:
        print("Список задач:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")
    else:
        print("Список задач пуст.")


def delete_task():
    """ Метод для удаления задачи """

    if tasks:
        view_tasks()
        index = int(input("Введите номер задачи для удаления: "))
        if 1 <= index <= len(tasks):
            del tasks[index - 1]
            print("Задача удалена успешно.")
        else:
            print("Некорректный номер задачи.")
    else:
        print("Список задач пуст.")
