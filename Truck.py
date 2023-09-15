class Truck:
    def __init__(self, id, speed, weight, capacity, packages, mileage, address, time):
        self.id = id
        self.speed = speed
        self.weight = weight
        self.capacity = capacity
        self.packages = packages
        self.mileage = mileage
        self.address = address
        self.time = time

    def __str__(self):
        return f"{self.id} | {self.speed} | {self.weight} | {self.capacity} | {self.packages} | {self.mileage} | {self.address} | {self.time}"

    
        