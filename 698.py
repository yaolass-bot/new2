import json
from multiprocessing.resource_tracker import register

filename='credentials.json'
credentials= {'username': 'Irina', 'password': '<PASSWORD>'}
with open(filename, 'w') as json_file:
          def create_user(username, password):
              user = {'username': username, 'password': password}

username=input('Enter your username: ')
password=input('Enter your password: ')
if username == credentials['username'] and password == credentials['password']:
    print(username)
    exeption=input('Do you have the correct credentials? (y/n): ')
    if exeption == 'n':
        register






























































