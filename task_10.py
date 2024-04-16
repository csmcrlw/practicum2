class MotorCycle:
    def __init__(self):
        self.name = "MotorCycle"

    def print_two_wheeler(self):
        return "two wheeler"


class Truck:
    def __init__(self):
        self.name = "Truck"

    def print_eight_wheeler(self):
        return "eight wheeler"


class Car:
    def __init__(self):
        self.name = "Car"

    def print_four_wheeler(self):
        return "four wheeler"


class Adapter:
    def __init__(self, obj, **adapted_methods):
        self.obj = obj
        self.__dict__.update(adapted_methods)

    def __getattr__(self, attr):
        return getattr(self.obj, attr)

    def original_dict(self):
        return self.obj.__dict__


if __name__ == "__main__":
    objects = []

    motorcycle = MotorCycle()
    objects.append(Adapter(motorcycle, wheels=motorcycle.print_two_wheeler))

    truck = Truck()
    objects.append(Adapter(truck, wheels=truck.print_eight_wheeler))

    car = Car()
    objects.append(Adapter(car, wheels=car.print_four_wheeler))

    for obj in objects:
        print(f"A {obj.name} is a {obj.wheels()} vehicle")
