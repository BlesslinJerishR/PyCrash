class Dog:
    """A simple attempt to model a Dog"""
    def __init__(self, name, age):
        """Initialize name and age for the dog"""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog to sit"""
        print(f"{self.name} is now sitting")

    def roll(self):
        """Simulate a dog to roll over"""
        print(f"{self.name} just rolled over !")


my_dog = Dog('Jimmy', 5)
your_dog = Dog('James', 10)

print(f"My Dog's name is {my_dog.name}")
print(f"My Dog's age is {my_dog.age}")
my_dog.sit()
my_dog.roll()

print()

print(f"My Dog's name is {your_dog.name}")
print(f"My Dog's age is {your_dog.age}")
your_dog.sit()
your_dog.roll()