import random
from json_parser import JSONParser

def generate_json_file(filename):
    data = generate_random_data()

    parser = JSONParser('')
    json_string = parser.custom_dumps(data)

    with open(filename, 'w') as file:
        file.write(json_string)
    print(f"Generated JSON file: {filename}")

    return json_string

def generate_random_data():
    data = {
    'student' : { 
        'name': random_name(),
        'age': random_age(),
        'address': random_address(),
        'score': random_score(),
        'subject': random_subject(),
        'contact': random_contact()
        }
    }
    return data

def random_name():
    names = ['Anna', 'Lea', 'Davit', 'Levon', 'Maria']
    return random.choice(names)


def random_age():
    return random.randint(16, 50)


def random_address():
    streets = ['Leningradyan', 'Komitas', 'Baghramyan', 'Abovyan', 'Azatutyan']
    cities = ['Yerevan', 'Gyumri', 'Vanadzor', 'Dilijan', 'Jermuk']

    address = {
        'street': random.choice(streets),
        'city': random.choice(cities),
        'zipcode': random.randint(10000, 99999)
    }

    return address


def random_score():
    return random.randint(0, 100)


def random_subject():
    subject = random.choice(['Math', 'Science', 'History', 'Art'])
    return subject


def random_contact():
    contact =  random.choice(['address', 'phone', 'email'])
    return contact
