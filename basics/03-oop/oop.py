from enum import Enum, unique

class Polygon:
    def __init__(self, no_of_sides):
        self.n = no_of_sides
        self.sides = [0 for _ in range(no_of_sides)]  

    def input_sides(self):
        for i in range(self.n):
            self.sides[i] = float(input(f"Enter side {str(i+1)}: "))

class Triangle(Polygon):
    def __init__(self):
        Polygon.__init__(self, 3)

    def find_area(self):
        a, b, c = self.sides
        s = (a + b + c) / 2
        area = (s*(s-a)*(s-b)*(s-c))**0.5
        print(f"The area of the triangle is {area}")

t = Triangle()
t.input_sides()
t.find_area()
print("=" * 50)

# @property
class Celsius:
    def __init__(self, temperature=0):
        self._temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

    @property
    def temperature(self):
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        if value < -273.15:
            raise ValueError("Temperature is below -273.15.")
        self._temperature = value

print("=" * 50)
c = Celsius(25)
print(c.to_fahrenheit())
c.temperature = 37
print(c.to_fahrenheit())

print("=" * 50)
# Customized class
class Student:
    __slots__ = ('name', 'age')

    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return f"Student object (name = {self.name})"

    __repr__ = __str__

    def __call__(self):
        print(f"My name is {self.name}")

    def __getattr__(self, attr):
        if attr == 'gender':
            return 'M'

s = Student("Signal")
s.age = 24
print(f"s = {s}")
print(f"s.name = {s.name}")
print(f"s.age = {s.name}")
print(f"s.gender = {s.gender}")
print(f"callable(s) = {callable(s)}")
s()
try:
    s.gender = 'M'
except AttributeError:
    print("Attribute Error...")
print("=" * 50)

class Fib:
    def __init__(self):
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 100000:
            raise StopIteration()
        return self.a
    
    def __getitem__(self, n):
        if isinstance(n, int):
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a

        if isinstance(n, slice):
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a+b
            return L

f = Fib()
print(f"f[5] = {f[5]}")
print(f"f[1:6] = {f[1:6]}")
print("=" * 50)

# Enum class
@unique
class Weekday(Enum):
    Sum = 0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6

day1 = Weekday.Mon
print(f"day1 = {day1}")
print(f"day1.value = {day1.value}")
