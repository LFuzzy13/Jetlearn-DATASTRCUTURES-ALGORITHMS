class Car:
    def __init__(self, brand):
        self.brand = brand
        self.speed = 0

    def accelerate(self):
        self.speed += 10
        print(f"Vroom! Speed is now {self.speed}.")

    def brake(self):
        self.speed -= 10
        print(f"Screech! Speed is now {self.speed}.")


# Create a car object
car = Car("Toyota")

# Accelerate 3 times
car.accelerate()
car.accelerate()
car.accelerate()

# Brake once
car.brake()