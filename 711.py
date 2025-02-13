import json


class myClass:
    def __init__(self,title,text,author):
        self.title = '1'
        self.text = '2'
        self.author = '3'

    def save (self, filename):
        data = {'name': self.title, 'age': self.text, 'city': self.author}
        with open(filename, 'w') as f:
            json.dump(data,f)

