""" Создадим класс Logger для записи событий работы приложения.
Используем паттерн Одиночка, т.к. нам нужно, чтобы все события записывались в один журнал """


class Logger:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
            cls._instance.log_file = "app.log"
        return cls._instance

    def write_log(self, message):
        with open(self.log_file, 'a') as f:
            f.write(message + '\n')


# Пример использования
if __name__ == "__main__":
    # Создание двух объектов Logger
    logger1 = Logger()
    logger2 = Logger()
    logger3 = Logger()

    # Проверка, что это один и тот же объект
    print(logger1 is logger2)
    print(logger2 is logger3)

    # Логирование сообщения
    logger1.write_log("Application started")
    logger2.write_log("User logged in")
    logger3.write_log("Synchronization started")
