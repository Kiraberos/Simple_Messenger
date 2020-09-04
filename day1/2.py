from day1 import oldmax
from random import randint

users = [
    {
        'name': 'Jack',
        'password': '1234567890',
        'age': 10
    },

    {
        'name': 'Helen',
        'password': '0987654321',
        'age': 100
    }
]

for i in range(100):
    users.append({
        'name': oldmax.generate_name(),
        'password': oldmax.generate_name(),
        'age': randint(1, 200)
    })

print(users)

print(oldmax.oldmax(users)['name'])
