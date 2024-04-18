class Cat:
    """
    Класс, представляющий кота

    Атрибуты:
        name (str): Имя кота
        age (int): Возраст кота (в годах)
        color (str): Окрас кота
        breed (str): Порода кота
    """

    def __init__(self, name, age, color, breed):
        """
        Инициализация нового объекта класса Кот

        Аргументы:
            name (str): Имя кота
            age (int): Возраст кота в годах
            color (str): Окрас кота
            breed (str): Порода кота
        """
        self.name = name
        self.age = age
        self.color = color
        self.breed = breed

    def sleep(self, hours):
        """
        Метод, симулирующий сон кота

        Аргументы:
            hours (int): Продолжительность сна (в часах)

        Что возвращает:
            str: Сообщение со временем сна кота в часах
        """
        return f"{self.name} спал {hours} часов."

    def meow(self):
        """ Симуляция мяуканья кота

         Возвращает:
             str: Сообщение о том, что кот <имя_кота> мяукает
        """
        return f"{self.name} мяукает."

    def eat(self, meals_number):
        """ Метод, симулирующий прием пищи кота

         Аргументы:
            meals_number (int): количество приемов пищи котом

        Возвращает:
            str: Сообщение о том, сколько раз кот поел
        """

        return f"{self.name} поел(а) {meals_number} раз(а)."


if __name__ == "__main__":
    """ Пример использования класса Cat """
    cat_vasya = Cat("Вася", 5, "полосатый", "домашний")
    print(cat_vasya.sleep(10))
    print(cat_vasya.eat(2))
    print(cat_vasya.meow())
