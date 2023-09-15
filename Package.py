import csv

class Package:
    loaded_time = None
    def __init__(self, id, address, city, state, zip, deadline, weight, status, notes, time):
        self.id = id
        self.address = address
        self.city = city    
        self.state = state
        self.zip = zip
        self.deadline = deadline
        self.weight = weight
        self.status = status
        self.notes = notes
        self.time = time

    def __str__(self):
        return f"{self.id} | {self.address} {self.city} {self.state} {self.zip} | {self.deadline} | {self.weight} kilos | {self.status} | Notes: {self.notes} | Time: {self.time}"

