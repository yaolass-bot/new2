import json

filename='credentials.json'
credentials= {'username':'Irina', 'password':'<PASSWORD>'}
with open(filename, 'w') as json_file:
    json.dump(credentials, json_file, indent=4)
print(f"Credentials saved to {filename}")















































