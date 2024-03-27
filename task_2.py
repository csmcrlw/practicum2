def plus_two(number):
    """Функция выполняет сложение числа 2 и значения переменной number."""
    try:
        result = 2 + number
        print("Результат:", result)
    except TypeError:
        print("Ожидаемый тип данных — число!")


# Пример использования
plus_two(10)  # Валидный вызов
plus_two(13.5)  # Валидный вызов
plus_two("5")  # Невалидный вызов
