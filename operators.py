
# --- ЗАДАНИЕ 1 ---

import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def circumference(self):
        return 2 * math.pi * self.radius

    def __eq__(self, other):
        if isinstance(other, Circle):
            return self.radius == other.radius
        return False

    def __lt__(self, other):
        return self.circumference < other.circumference

    def __gt__(self, other):
        return self.circumference > other.circumference

    def __le__(self, other):
        return self.circumference <= other.circumference

    def __ge__(self, other):
        return self.circumference >= other.circumference

    def __add__(self, value):
        return Circle(self.radius + value)

    def __sub__(self, value):
        return Circle(self.radius - value)

    def __iadd__(self, value):
        self.radius += value
        return self

    def __isub__(self, value):
        self.radius -= value
        return self

    def __str__(self):
        return f"Круг(R={self.radius:.2f})"


# --- ЗАДАНИЕ 2 ---

class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
        return Complex(self.real - other.real, self.imag - other.imag)

    def __mul__(self, other):
        return Complex(self.real * other.real - self.imag * other.imag,
                       self.real * other.imag + self.imag * other.real)

    def __truediv__(self, other):
        denominator = other.real**2 + other.imag**2
        if denominator == 0:
            raise ValueError("Деление на ноль невозможно")
        
        new_real = (self.real * other.real + self.imag * other.imag) / denominator
        new_imag = (self.imag * other.real - self.real * other.imag) / denominator
        return Complex(new_real, new_imag)

    def __str__(self):
        sign = "+" if self.imag >= 0 else ""
        return f"({self.real}{sign}{self.imag}i)"


# --- ЗАДАНИЕ 3 ---

class Airplane:
    def __init__(self, plane_type, max_passengers, current_passengers=0):
        self.plane_type = plane_type
        self.max_passengers = max_passengers
        self.current_passengers = current_passengers

    def __eq__(self, other):
        return self.plane_type == other.plane_type

    def __add__(self, value):
        return Airplane(self.plane_type, self.max_passengers, self.current_passengers + value)
    
    def __sub__(self, value):
        return Airplane(self.plane_type, self.max_passengers, self.current_passengers - value)

    def __iadd__(self, value):
        if self.current_passengers + value <= self.max_passengers:
            self.current_passengers += value
        else:
            print("Ошибка: Слишком много пассажиров!")
        return self

    def __isub__(self, value):
        if self.current_passengers - value >= 0:
            self.current_passengers -= value
        else:
            print("Ошибка: Пассажиров не может быть меньше 0!")
        return self

    def __gt__(self, other):
        return self.max_passengers > other.max_passengers

    def __lt__(self, other):
        return self.max_passengers < other.max_passengers
    
    def __ge__(self, other):
        return self.max_passengers >= other.max_passengers

    def __le__(self, other):
        return self.max_passengers <= other.max_passengers

    def __str__(self):
        return f"Самолет {self.plane_type}: {self.current_passengers}/{self.max_passengers} пас"


# --- ЗАДАНИЕ 4 ---

class Flat:
    def __init__(self, area, price):
        self.area = area
        self.price = price

    def __eq__(self, other):
        return self.area == other.area

    def __ne__(self, other):
        return self.area != other.area

    def __gt__(self, other):
        return self.price > other.price

    def __lt__(self, other):
        return self.price < other.price
    
    def __ge__(self, other):
        return self.price >= other.price

    def __le__(self, other):
        return self.price <= other.price

    def __str__(self):
        return f"Квартира {self.area}м2 за {self.price}$"


# ПРОВЕРКА
if __name__ == "__main__":
    
    print("\n--- Задание 1: Круг ---")
    c1 = Circle(10)
    c2 = Circle(15)
    print(f"Круг 1: {c1}, Круг 2: {c2}")
    print(f"Равны ли радиусы? {c1 == c2}")
    print(f"Круг 1 меньше Круга 2? {c1 < c2}")
    c1 += 5
    print(f"Круг 1 после (+5): {c1}")

    print("\n--- Задание 2: Комплексные числа ---")
    num1 = Complex(2, 3)
    num2 = Complex(1, 4)
    print(f"Сумма: {num1 + num2}")
    print(f"Умножение: {num1 * num2}")

    print("\n--- Задание 3: Самолет ---")
    plane1 = Airplane("Boeing 747", 500, 100)
    plane2 = Airplane("Airbus A320", 180, 100)
    print(f"Одинаковый тип? {plane1 == plane2}")
    print(f"Boeing вместительнее Airbus? {plane1 > plane2}") 
    
    plane2 += 50 
    print(f"Airbus после посадки: {plane2}")

    print("\n--- Задание 4: Квартира ---")
    flat1 = Flat(50, 60000)
    flat2 = Flat(50, 45000)
    print(f"Площади равны? {flat1 == flat2}")
    print(f"Первая дороже второй? {flat1 > flat2}")