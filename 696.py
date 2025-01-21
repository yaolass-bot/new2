import json

filename='credentials.json'
credentials= {'username':'Irina', 'password':'<PASSWORD>'}
with open(filename, 'w') as json_file:
    json.dump(credentials, json_file, indent=4)
print(f"Credentials saved to {filename}")
username = 'user1'
password = '<PASSWORD>'

if username == 'user1':
    print("Login successfully")
else:
    print("Login failed")

users = {"alisa","bob", "charlie"}
user_to_check = "bob"

if user_to_check in users:
    print(f"User {user_to_check} exists")
else:
    print(f"User {user_to_check} doesn't exist")













































