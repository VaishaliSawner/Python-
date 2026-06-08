class Animal:
    def sound(self):
        pass


class Dog(Animal):
        def sound(self):
            print("bark")


    
class Cat(Animal):
        def sound(self):
            print("meow")

    
class Cow(Animal):
        def sound(self):
            print("moo")

    


dog=Dog()
dog.sound()


cat=Cat()
cat.sound()


cow=Cow()
cow.sound()


