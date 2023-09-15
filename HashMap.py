import csv
import Package


class HashMap:

    def __init__(self):
        self.size = 256 
        self.map = [None] * self.size 

    def get_hash(self, key):
        hash = 0
        for char in str(key):
            hash += ord(char)
        return hash % self.size

    def add(self, key, value):
        index = self.get_hash(key)
        kv_pair = [key, value]

        if self.map[index] is None:
            self.map[index] = list([kv_pair])
            return True
        else:
            for pair in self.map[index]:
                if pair[0] == key:
                    pair[1] = value
                    return True
            self.map[index].append(kv_pair)
            return True
        
    def get(self, key):
        index = self.get_hash(key)
        if self.map[index] is not None:
            for pair in self.map[index]:
                if pair[0] == key:
                    return pair[1]
        return None
    
    def delete(self, key):
        index = self.get_hash(key)
        if self.map[index] is not None:
            for pair in self.map[index]:
                if pair[0] == key:
                    self.map[index].pop(pair)
                    return True
        return False
