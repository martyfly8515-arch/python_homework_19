import json


# ==========================================
# ЗАДАНИЕ 1. DEVICE И НАСЛЕДОВАНИЕ
# ==========================================

class Device:
    def __init__(self, brand, model, power):
        self.brand = brand
        self.model = model
        self.power = power

    def show_info(self):
        print(
            f"Бренд: {self.brand}, "
            f"модель: {self.model}, "
            f"мощность: {self.power} Вт"
        )

    def turn_on(self):
        print(f"{self.model} включено")


class CoffeeMachine(Device):
    def make_coffee(self):
        print("Кофемашина готовит кофе")


class Blender(Device):
    def blend(self):
        print("Блендер измельчает продукты")


class MeatGrinder(Device):
    def grind_meat(self):
        print("Мясорубка перемалывает мясо")


print("Задание 1")

coffee_machine = CoffeeMachine("DeLonghi", "EC685", 1300)
coffee_machine.show_info()
coffee_machine.turn_on()
coffee_machine.make_coffee()

blender = Blender("Bosch", "MSM", 800)
blender.show_info()
blender.blend()

meat_grinder = MeatGrinder("Moulinex", "ME1068", 1400)
meat_grinder.show_info()
meat_grinder.grind_meat()


# ==========================================
# ЗАДАНИЕ 2. SHIP И НАСЛЕДОВАНИЕ
# ==========================================

class Ship:
    def __init__(self, name, speed, crew):
        self.name = name
        self.speed = speed
        self.crew = crew

    def show_info(self):
        print(
            f"Корабль: {self.name}, "
            f"скорость: {self.speed} узлов, "
            f"экипаж: {self.crew}"
        )

    def move(self):
        print(f"{self.name} движется по морю")


class Frigate(Ship):
    def patrol(self):
        print(f"Фрегат {self.name} выполняет патрулирование")


class Destroyer(Ship):
    def attack(self):
        print(f"Эсминец {self.name} готов к атаке")


class Cruiser(Ship):
    def long_voyage(self):
        print(f"Крейсер {self.name} отправился в дальний поход")


print("\nЗадание 2")

frigate = Frigate("Admiral", 30, 180)
frigate.show_info()
frigate.patrol()

destroyer = Destroyer("Defender", 35, 250)
destroyer.show_info()
destroyer.attack()

cruiser = Cruiser("Ocean", 32, 500)
cruiser.show_info()
cruiser.long_voyage()


# ==========================================
# МНОЖЕСТВЕННОЕ НАСЛЕДОВАНИЕ
# ЗАДАНИЕ 1
# ОКРУЖНОСТЬ, ВПИСАННАЯ В КВАДРАТ
# ==========================================

class CircleBase:
    def __init__(self, radius):
        self.radius = radius

    def circle_area(self):
        return 3.14 * self.radius ** 2


class SquareBase:
    def __init__(self, side):
        self.side = side

    def square_area(self):
        return self.side ** 2


class CircleInSquare(CircleBase, SquareBase):
    def __init__(self, radius):
        CircleBase.__init__(self, radius)
        SquareBase.__init__(self, radius * 2)

    def show_info(self):
        print(f"Радиус окружности: {self.radius}")
        print(f"Сторона квадрата: {self.side}")
        print(f"Площадь окружности: {self.circle_area()}")
        print(f"Площадь квадрата: {self.square_area()}")


print("\nМножественное наследование. Задание 1")

figure = CircleInSquare(5)
figure.show_info()


# ==========================================
# МНОЖЕСТВЕННОЕ НАСЛЕДОВАНИЕ
# ЗАДАНИЕ 2. АВТОМОБИЛЬ
# ==========================================

class Wheels:
    def __init__(self, wheel_count):
        self.wheel_count = wheel_count

    def wheels_info(self):
        print(f"Количество колёс: {self.wheel_count}")


class Engine:
    def __init__(self, engine_power):
        self.engine_power = engine_power

    def engine_info(self):
        print(f"Мощность двигателя: {self.engine_power} л.с.")


class Doors:
    def __init__(self, door_count):
        self.door_count = door_count

    def doors_info(self):
        print(f"Количество дверей: {self.door_count}")


class Car(Wheels, Engine, Doors):
    def __init__(self, brand, wheel_count, engine_power, door_count):
        self.brand = brand
        Wheels.__init__(self, wheel_count)
        Engine.__init__(self, engine_power)
        Doors.__init__(self, door_count)

    def show_info(self):
        print(f"Автомобиль: {self.brand}")
        self.wheels_info()
        self.engine_info()
        self.doors_info()


print("\nМножественное наследование. Задание 2")

car = Car("Audi", 4, 190, 4)
car.show_info()


# ==========================================
# МНОЖЕСТВЕННОЕ НАСЛЕДОВАНИЕ
# ЗАДАНИЕ 3. SHAPE
# ==========================================

class Shape:
    def show(self):
        print(self.__dict__)

    def save(self, filename):
        data = {
            "type": self.__class__.__name__,
            "data": self.__dict__
        }

        with open(filename, "a", encoding="utf-8") as file:
            file.write(json.dumps(data, ensure_ascii=False) + "\n")

    @staticmethod
    def load(filename):
        figures = []

        with open(filename, "r", encoding="utf-8") as file:
            for line in file:
                item = json.loads(line)
                figure_type = item["type"]
                data = item["data"]

                if figure_type == "Square":
                    figure = Square(
                        data["x"],
                        data["y"],
                        data["side"]
                    )
                elif figure_type == "Rectangle":
                    figure = Rectangle(
                        data["x"],
                        data["y"],
                        data["width"],
                        data["height"]
                    )
                elif figure_type == "Circle":
                    figure = Circle(
                        data["x"],
                        data["y"],
                        data["radius"]
                    )
                elif figure_type == "Ellipse":
                    figure = Ellipse(
                        data["x"],
                        data["y"],
                        data["width"],
                        data["height"]
                    )
                else:
                    continue

                figures.append(figure)

        return figures


class Square(Shape):
    def __init__(self, x, y, side):
        self.x = x
        self.y = y
        self.side = side

    def show(self):
        print(
            f"Квадрат: x={self.x}, y={self.y}, "
            f"сторона={self.side}"
        )


class Rectangle(Shape):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def show(self):
        print(
            f"Прямоугольник: x={self.x}, y={self.y}, "
            f"ширина={self.width}, высота={self.height}"
        )


class Circle(Shape):
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

    def show(self):
        print(
            f"Окружность: центр=({self.x}, {self.y}), "
            f"радиус={self.radius}"
        )


class Ellipse(Shape):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def show(self):
        print(
            f"Эллипс: x={self.x}, y={self.y}, "
            f"ширина={self.width}, высота={self.height}"
        )


print("\nМножественное наследование. Задание 3")

figures = [
    Square(10, 20, 5),
    Rectangle(5, 8, 20, 10),
    Circle(15, 15, 7),
    Ellipse(2, 4, 30, 15)
]

filename = "figures.txt"

open(filename, "w", encoding="utf-8").close()

for figure in figures:
    figure.save(filename)

print("\nФигуры сохранены в файл.")

loaded_figures = Shape.load(filename)

print("\nФигуры, загруженные из файла:")

for figure in loaded_figures:
    figure.show()
