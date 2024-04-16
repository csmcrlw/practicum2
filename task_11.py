# Базовый компонент
class Coffee:
    def show_cost(self):
        return 5

    def show_description(self):
        return "Coffee"


# Декораторы
class MilkDecorator:
    def __init__(self, coffee):
        self.coffee = coffee

    def show_cost(self):
        return self.coffee.show_cost() + 2

    def show_description(self):
        return self.coffee.show_description() + ", Milk"


class SugarDecorator:
    def __init__(self, coffee):
        self.coffee = coffee

    def show_cost(self):
        return self.coffee.show_cost() + 1

    def show_description(self):
        return self.coffee.show_description() + ", Sugar"


class VanillaDecorator:
    def __init__(self, coffee):
        self.coffee = coffee

    def show_cost(self):
        return self.coffee.show_cost() + 3

    def show_description(self):
        return self.coffee.show_description() + ", Vanilla"


if __name__ == "__main__":
    # Создание кофе с добавками
    coffee = Coffee()
    coffee_with_milk = MilkDecorator(coffee)
    coffee_with_milk_and_sugar = SugarDecorator(coffee_with_milk)
    coffee_with_all_options = VanillaDecorator(coffee_with_milk_and_sugar)

    print("Description:", coffee_with_all_options.show_description())
    print("Cost:", coffee_with_all_options.show_cost())
