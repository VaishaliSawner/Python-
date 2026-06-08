class Vehicle:
    def start(self):
      pass
    def stop(self):
      pass
    

class Car(Vehicle):
    def start(self):
        print("Car started")
    def stop(self):
        print("Car stopped")

class Bike(Vehicle):
    def start(self):
        print("Bike started")
    def stop(self):
        print("Bike stopped")


class Bus(Vehicle):
    def start(self):
       print("Bus started")
    def stop(self):
       print("BUs stopped")


bus=Bus()
bus.stop()
bus.start()

car=Car()
car.stop()
car.start()

bike=Bike()
bike.stop()
bike.start()