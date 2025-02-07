# 1. Создайте базовый класс `Animal`, который будет содержать общие атрибуты (например, `name`, `age`) и методы (`make_sound()`, `eat()`)
# для всех животных.
# 2. Реализуйте наследование, создав подклассы `Bird`, `Mammal`, и `Reptile`, которые наследуют от класса `Animal`.
# Добавьте специфические атрибуты и переопределите методы, если требуется (например, различный звук для `make_sound()`).
# 3. Продемонстрируйте полиморфизм: создайте функцию `animal_sound(animals)`, которая принимает список животных и вызывает метод `make_sound()`
# для каждого животного.
# 4. Используйте композицию для создания класса `Zoo`, который будет содержать информацию о животных и сотрудниках.
# Должны быть методы для добавления животных и сотрудников в зоопарк.
# 5. Создайте классы для сотрудников, например, `ZooKeeper`, `Veterinarian`, которые могут иметь специфические
# методы (например, `feed_animal()` для `ZooKeeper` и `heal_animal()` для `Veterinarian`)

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        pass

    def eat(self):
        pass

    def info(self):
        return f'{self.name}, возраст: {self.age} года/лет\n'


class Bird(Animal):
    def __init__(self, name, age, colour):
        super().__init__(name, age)
        self.colour = colour

    def make_sound(self):
        print('Издает звуки: фью-фью')

    def eat_bird(self):
        print(f'{self.name} питается зернами и насекомыми')

    def info(self):
        return super().info() + f'Окрас: {self.colour}\n'


class Mammal(Animal):
    def __init__(self, name, age, dimension):
        super().__init__(name, age)
        self.dimension = dimension

    def eat_mammal(self):
        print(f'{self.name} питается травой и листьями')

    def make_sound(self):
        print(f'Звучит как {self.name}')

    def info(self):
        return super().info() + f'Размерность: {self.dimension} млекопитающее\n'


class Reptile(Animal):
    def __init__(self, name, age, reptile_type):
        super().__init__(name, age)
        self.type = reptile_type

    def make_sound(self):
        print(f'Звучит как {self.name}')

    def eat_reptile(self):
        print(f'{self.name} питается насекомыми')

    def info(self):
        return super().info() + f'Тип пресмыкающегося: {self.type}\n'


def animal_sound(animals):
    for animal in animals:
        print(f'{animal.name}', end=' ')
        animal.make_sound()


class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def info(self):
        return f'Сотрудник: {self.name}, должность: {self.position}\n'

class ZooKeeper(Employee):
    def feed_animal(self, animal):
        print(f'{self.name} кормит {animal.name}')


class Veterinarian(Employee):
    def heal_animal(self, animal):
        print(f'{self.name} лечит {animal.name}')


class Zoo:
    def __init__(self):
        self.animals = []
        self.employees = []

    def add_animal(self, animal):
        self.animals.append(animal)
        print(f'Животное {animal.name} добавлено в зоопарк.')

    def add_employee(self, employee):
        self.employees.append(employee)
        print(f'Сотрудник {employee.name} добавлен в зоопарк.')

    def show_animals(self):
        result = 'Животные в зоопарке:\n'
        for animal in self.animals:
            result += animal.info()
        return result

    def show_employees(self):
        result = 'Сотрудники зоопарка:\n'
        for employee in self.employees:
            result += employee.info()
        return result


zoo = Zoo()

bird1 = Bird("Лебедь", "2", "Белый")
bird2 = Bird("Павлин", "3", "Многоцветный")
mammal1 = Mammal("Слон", "10", "крупное")
mammal2 = Mammal("Козел", "2", "среднее")
reptile1 = Reptile("Кобра", "2", "наземное")

animals = [bird1, bird2, mammal1, mammal2, reptile1]
animal_sound(animals)

zoo.add_animal(bird1)
zoo.add_animal(bird2)
zoo.add_animal(mammal1)
zoo.add_animal(mammal2)
zoo.add_animal(reptile1)

zookeeper = ZooKeeper("Мария", "Уход за животными")
veterinarian = Veterinarian("Иван", "Ветеринар")

zoo.add_employee(zookeeper)
zoo.add_employee(veterinarian)

# Запись информации о животных и сотрудниках в файл
with open("zoo_info.txt", "w", encoding="utf-8") as file:
    file.write(zoo.show_animals())
    file.write(zoo.show_employees())
    