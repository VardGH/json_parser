# json_parser
The program allows you to parse a JSON string, add, update and delete parsed data fields and save the changed data to a file.

## Usage
1. Clone this repository.
2. Create a JSON file or use an existing one.
3. Run the script by executing the command python3 json_parser.py
4. Enter commands as prompted to add, update, or delete fields in the JSON data.
5. To exit the program, enter the command exit.

## Example Commands
- student.name = Anna: Adds or updates the "name" field in the "student" object with the value "Anna".
- del student: Deletes the "student" object from the JSON data.
- upd school.name = Academy: Updates the "name" field in the "school" object with the value "Academy".

## Generating Random JSON Data
You can use the random_json.py script to generate a random JSON file for testing purposes. Here's how to use it:

1. Clone this repository.
2. Run the script by executing the command python3 random_json.py.
3. The script will generate a random JSON file named json.txt in the same directory.

## Testing
The JSONParser class can be tested using the following step.
- Run the test program: python3 test.py
