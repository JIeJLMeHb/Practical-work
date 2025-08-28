class Animal:
    def __init__(self, name, age, species):
        self.name = name
        self.age = age
        self.species = species
        print(f"Создание объекта Animal: {self.name}")

    def make_sound(self):
        print("*звук животного*")

    def info(self):
        print(f"Животное: {self.name}\nВозраст: {self.age}\nВид: {self.species}")

    def __del__(self):
        print(f"Удаление объекта Animal: {self.name}")


class Dog(Animal):
    def __init__(self, name, age, species, breed, guard_status):
        super().__init__(name, age, species)
        self.breed = breed
        self.guard_status = guard_status
        print(f"Создание объекта Dog: {self.name}")

    def info(self):
        print(f"Собака\nВозраст: {self.age}\nВид: {self.species}\nРазмножается: {self.breed}\nОхраняет: {self.guard_status}")

    def guard_house(self):
        print(f"Текущий статус охраны: {self.guard_status}")
        selector = input("Сменить статус? Y/N: ")
        if selector == 'Y':
            self.guard_status = input("Введите новый статус: ")
        print(f"Текущий статус охраны: {self.guard_status}")
        
    def __del__(self):
        print(f"Удаление объекта Dog: {self.name}")
        