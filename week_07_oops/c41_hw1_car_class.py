# Ek Car class banao with brand, speed, aur ek method drive() jo "BRAND is driving at SPEED" print kare.

class Car:
    def __init__(self,brand,speed):
        self.brand = brand
        self.speed = speed

    def drive(self):
        print(f"{self.brand} is driving at {self.speed}")

car_obj = Car("maruti",60)

car_obj.drive()