
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def display(self):
        print(f"{self.name}")
        print(f"{self.breed}")


# Creating objects
d1 = Dog("Tommy", "Labrador")
d2 = Dog("Rocky", "Pug")



# Display
d1.display()
d2.display()