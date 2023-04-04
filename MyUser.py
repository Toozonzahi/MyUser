import requests

# Question 1
res = requests.get('https://jsonplaceholder.typicode.com/users') # Url for all the data

class MyUser:
    def __init__(self, id, email, username, name):
        self.id = id
        self.email = email
        self.username = username
        self.name = name

    def __str__(self):
        return f'id: {self.id} email: {self.email} username: {self.username} name: {self.name}'

users = res.json()
for user in users:
    my_user = MyUser(user['id'], user['email'], user['username'], user['name'])
    print(my_user)

# Question 2
entuser = input('Please enter your name: ')
for user in users:
    if user['name'] == entuser:
        print(f' User {entuser} found')
        break
    else:
        print('User not found')
