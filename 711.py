import json


class myClass:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.city = 'San Francisco'

    def save (self, filename):
        data = {'name': self.name, 'age': self.age, 'city': self.city}
        with open(filename, 'w') as f:
            json.dump(data, f)

