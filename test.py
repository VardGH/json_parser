import random
from json_parser import JSONParser
from random_json import generate_json_file, random_name, random_age, random_score, random_subject, random_contact

def generate_test_commands(json_data):
    commands = []

    for _ in range(random.randint(1, 10)):
        random_command = random.choice(['add', 'upd', 'del'])
        field = get_random_field()
        if random_command == 'add':
            command = f'{field}'
        elif random_command == 'upd':
            command = f'upd {field}'
        else:
            command = field.split('=')[0].strip()
            command = f'del {command}'
        commands.append(command)

    return commands

def get_random_field():
    field = random.choice(['name', 'age', 'address', 'score', 'subject', 'contact'])
    if field == 'name':
        return f'student.{field} = {random_name()}'
    if field == 'age':
        return f'student.{field} = {random_age()}'
    if field == 'address':
        address_nesred = random.choice(['street', 'city', 'zipcode'])
        if address_nesred == 'street':
            streets = ['Komitas', 'Baghramyan', 'Abovyan', 'Azatutyan']
            return f'student.{field}.{address_nesred} = {random.choice(streets)}'
        elif address_nesred == 'city':
            cities = ['Yerevan', 'Gyumri', 'Vanadzor', 'Dilijan']
            return f'student.{field}.{address_nesred} = {random.choice(cities)}'
        else:
            return f'student.{field}.{address_nesred} = {random.randint(10000, 99999)}'
    if field == 'score':
        return f'student.{field} = {random_score()}'
    if field == 'subject':
        return f'student.{field} = {random_subject()}'
    if field == 'contact':
        return f'student.{field} = {random_contact()}'
    
def test_json_parser(json_string, commands, filename):
    parser = JSONParser(json_string)
    parsed_data = parser.parse()

    if parsed_data is None:
        print("Invalid JSON file. Program terminated.")
        return

    print("\nInitial JSON data:")
    print(parser.custom_dumps(parsed_data))

    for command in commands:
        print(f"\nExecuting command: {command}")
        parser.process_command(parsed_data, command, filename)

def run_test_program():
    filename = 'json.txt'
    json_string = generate_json_file(filename)
    commands = generate_test_commands(json_string)
    test_json_parser(json_string, commands, filename)


run_test_program()