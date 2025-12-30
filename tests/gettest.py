import json

def get_pw(program_name):
    try:
        with open(f'test.json', 'r') as f:
            data = json.load(f)
            password = data[1][program_name]

            print(password)
    except FileNotFoundError:
        print(f'You have no passwords saved!')
    except TypeError:
        TypeError
    except json.JSONDecodeError:
        print(f'Error: could not decode JSON from the file')

print(get_pw("2"))