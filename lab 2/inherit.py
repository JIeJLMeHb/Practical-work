class Animal:
    def __init__(self, name, age, species):
        self.name = name
        self.age = age
        self.species = species
    
    def make_sound(self):
        print('Making sound')

    def info(self):
        print('Name:', self.name)
        print('Age:', self.age)
        print('Specie:', self.species)

class Dog(Animal):
    def __init__(self, name, age, species, breed, guard_status):
        super().__init__(name, age, species)
        self.breed = breed
        self.guard_status = guard_status
    
    def get_info(self):
        super().info()
        print('Breed: ', self.breed)
        print('Guard_status: ', self.guard_status)
    
    def make_sound(self):
        super().make_sound()
    
    def guard_house(self):
        if self.guard_status == 'Active':
            print('Guarding house')
        else:
            print('Chilling')

def main():
    user_choose = input("For animal enter 1, for dog enter 2: ")
    if user_choose == '1':
        name = input('Enter name: ')
        age = input('Enter age: ')
        specie = input('Enter specie: ')
        animal = Animal(name, age, specie)
        animal.info()
        animal.make_sound()
    elif user_choose == '2':
        name = input('Enter name: ')
        age = input('Enter age: ')
        specie = 'Dog'
        breed = input('Enter breed: ')
        guard_status = input('Enter guard status: ')
        animal = Dog(name, age, specie, breed, guard_status)
        animal.info()
        animal.make_sound()
        animal.guard_house()

if __name__ == "__main__":
    main()
