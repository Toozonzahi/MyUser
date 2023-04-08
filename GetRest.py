import requests

# Question 5
entuser = int(input('Please enter a number under 100: ')) # User Input

for i in range(entuser):
    res = requests.get('https://randomuser.me/api')  # Url for all the data
    users = res.json()
    names = users['results'][0]['name']['first'] + ' ' + users['results'][0]['name']['last']    #Get First Name + Last Name
    if entuser <= 100:
        print(names)
    else:
        print('Please provide a number under 100')
        break