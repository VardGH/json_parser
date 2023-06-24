class JSONParser:
    def __init__(self, json_string):
        self.json_string = self.remove_whitespaces(json_string)
        self.index = 0

    def parse(self):
        if self.json_string[0] == "{" and self.json_string[-1] == "}":
            return self.parse_value()
        else:
            print("Invalid JSON file")
            return None
    
    def remove_whitespaces(self, json_string):
        res = json_string.replace("\n", "")
        res = res.replace(" ", "")
        return res.replace("\t", "")

    def parse_value(self):
        if self.index < len(self.json_string):
            if self.json_string[self.index] == '{':
                return self.parse_object()
            elif self.json_string[self.index] == '"':
                return self.parse_string()
            elif self.json_string[self.index] in ('-', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'):
                return self.parse_number()

    def parse_object(self):
        obj = {}
        self.index += 1
        while self.index < len(self.json_string):
            if self.json_string[self.index] == '}':
                self.index += 1
                return obj

            key = self.parse_string()
            if self.json_string[self.index] != ":":
                print("Invalid JSON file")
                return

            self.index += 1  # Skip the ':' character

            value = self.parse_value()
            obj[key] = value
            if self.json_string[self.index] == '}':
                self.index += 1
                return obj
            self.index += 1  # Skip the ',' character

    def parse_string(self):
        start = self.index + 1
        end = self.json_string.find('"', start)
        self.index = end + 1
        return self.json_string[start:end]
    

    def parse_number(self):
        start = self.index
        while self.json_string[self.index] in ('-', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.'):
            self.index += 1
        end = self.index
        return float(self.json_string[start:end])

    def add_field(self, parsed_data, field_expr, field_value):
        nested_fields = field_expr.split('.')
        
        for i in range(len(nested_fields) - 1):
            if nested_fields[i] not in parsed_data:
                parsed_data[nested_fields[i]] = {}
            parsed_data = parsed_data[nested_fields[i]]

        parsed_data[nested_fields[-1]] = field_value
        print(f"Field '{field_expr}' added successfully.")


    def update_field(self, parsed_data, field_expr, field_value):
        field = field_expr.split('.')
        if not isinstance(field, list) or len(field) < 2:
            print("Invalid command. Please provide a valid field name and value.")
            return
        
        for nested_field in field[:-1]:
            if nested_field in parsed_data:
                parsed_data = parsed_data[nested_field]
            else:
                print(f"Nested field '{nested_field}' does not exist.")
                return

        final_field = field[-1] 
        if final_field in parsed_data:
            parsed_data[final_field] = field_value
            print(f"Nested field '{final_field}' updated successfully.")
        else:
            print(f"Nested field '{final_field}' does not exist.")


    def delete_field(self, parsed_data, field_expr):
        field = field_expr.split('.')
        if len(field) < 1:
            print("Invalid command. Please provide a valid field name.")
            return
        
        for nested_field in field[:-1]:
            if nested_field in parsed_data:
                parsed_data = parsed_data[nested_field]
            else:
                print(f"Nested field '{nested_field}' does not exist.")
                return

        if field[-1] in parsed_data:
            del parsed_data[field[-1]]
            print(f"Field '{field_expr}' deleted successfully.")
        else:
            print(f"Field '{field_expr}' does not exist.")


    def process_command(self, parsed_data, command, path):
        command = command.strip()  # Trim any leading or trailing spaces

        if command.startswith('upd'):
            parts = command[3:].strip().split('=')
            if len(parts) != 2:
                print("Invalid command. Please provide a valid field name and value.")
                return

            expr = parts[0].strip()
            value = parts[1].strip()

            self.update_field(parsed_data, expr, value)

        elif command.startswith('del'):
            expr = command[3:].strip()
            if not expr:
                print("Invalid command. Please provide a valid field name.")
                return

            self.delete_field(parsed_data, expr)

        else:
            parts = command.split('=')
            if len(parts) != 2:
                print("Invalid command. Please provide a valid command.")
                return

            expr = parts[0].strip()
            value = parts[1].strip()

            self.add_field(parsed_data, expr, value)

        with open(path, 'w') as file:
            file.write(self.custom_dumps(parsed_data))

    def custom_dumps(self, parsed_data, indent=4):
        def _dump_dict(d, level=0):
            result = ''
            for key, value in d.items():
                if isinstance(value, dict):
                    result += '\t' * level + f'"{key}": ' + _dump_dict(value, level + 1) + ',\n'
                else:
                    # Check if the value is a string
                    if isinstance(value, str):
                        result += '\t' * level + f'"{key}": "{value}",\n'  # Wrap the value in double quotes
                    elif isinstance(value, (int, float)):
                        tmp = int(value)
                        result += '\t' * level + f'"{key}": {tmp},\n'  # Number value without double quotes
                    else:
                        result += '\t' * level + f'"{key}": {value},\n'
            return '{\n' + result.rstrip(',\n') + '\n' + '\t' * (level - 1) + '}'

        return _dump_dict(parsed_data)

def main():
    path = 'data.txt'
    with open(path) as file:
        json_string = file.read()

    parser = JSONParser(json_string)
    parsed_data = parser.parse()

    if parsed_data is None:
        print("Invalid JSON file. Program terminated.")
        return

    while True:
        command = input("Enter a command (e.g. 'student.name = Anna', 'del student', 'upd school.name = Academy', 'exit'): ")

        if command == 'exit':
            break

        parser.process_command(parsed_data, command, path)

    print("Exit")


if __name__ == "__main__":
    main()
