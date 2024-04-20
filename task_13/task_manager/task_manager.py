# Модуль task_manager.py
import tasks
from task_13 import docs


def main():
    print("Добро пожаловать в менеджер задач!")

    while True:
        print("\nВыберите действие:")
        print("1. Добавить задачу")
        print("2. Просмотреть задачи")
        print("3. Удалить задачу")
        print("4. Справка")
        print("5. Выйти")

        choice = input("Введите номер действия: ")

        if choice == "1":
            tasks.add_task()
        elif choice == "2":
            tasks.view_tasks()
        elif choice == "3":
            tasks.delete_task()
        elif choice == "4":
            docs.show_help()
        elif choice == "5":
            print("До свидания!")
            break
        else:
            print("Некорректный ввод. Попробуйте снова.")


if __name__ == '__main__':
    main()
