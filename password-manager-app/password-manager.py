import json
from types import SimpleNamespace
from getpass import getpass

jsondata = {}

# Class for user of app
class AppUser: 
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def to_dict(self):
        return self.__dict__
# encodes for use in json file  
def encode_app_user(obj):
    if isinstance(obj, AppUser):
        return obj.to_dict()
    raise TypeError(f"Object of object {obj.__class__.__name__} is not json serializable")

class SaveData:
    def __init__(self, program, password):
        self.program = program
        self.password = password

    # def to_dict(self):
    #     return self.__dict__

# def encode_saved_item(obj):
#     if isinstance(obj, SavedItem):
#         return obj.to_dict()
#     raise TypeError(f"object of objecy {obj.__class__.__name__} is not json serializable")

def print_lines():
    print("------------------")

def new_pw_to_file(saved, jsondata):
    jsondata = {}
    password = {"password" : saved.password}
    jsondata[saved.program] = password
    try:
        with open(f'saved.json', "r") as f:
            data = json.load(f)
            if not isinstance(data, list):
                # ensure root element is a list
                data = []
    except FileNotFoundError:
        # if there is no file then start with an empty list
        data = []
    except json.JSONDecodeError:
        # if the file is corrupted or empty, start with an empty list
        data = []
    # convert new class instance to dictionary
    # append the data
    new_data = jsondata
    data.append(new_data)
    print(jsondata)
    # write to file
    with open('saved.json', 'w') as f:
        json.dump(data, f, indent = 2)

def retrieve_pw(program_name):
    try:
        with open(f'saved.json', 'r') as f:
            data = json.loads(f)
            password = data[str(program_name)][0]
            print(password)
            return password
    except FileNotFoundError:
        print(f'You have no passwords saved!')
    except TypeError:
        TypeError
    except json.JSONDecodeError:
        print(f'Error: could not decode JSON from the file')


def prompt():
    print("What would you like to do?")
    print("1. Save new password")
    print("2. Get password")
    print("3. Delete password")
    print("4. End program")

def first_time():   
    print("Welcome! I see you haven't used this application yet, Let's get you set up!")
    # setting user's name
    print("What is your name?")
    print_lines()
    user_name = input()
    # check to see if input is empty or not
    while user_name == "":
        print("Please input a name")
        print_lines()
        user_name = input()
    # setting user's pw
    print("Please set a password:")
    print_lines()
    user_pw = getpass()
    # check to see if input is empty or not
    while user_pw == "":
        print("Please input a password")
        print_lines()
        user_pw = input()
    user = AppUser(str(user_name), str(user_pw))
    print("We're done setting up " + user_name + "!")
    with open(f'app-user.json', 'w', encoding='utf-8') as f:
        json.dump(user, f, default=encode_app_user, indent=4)

def password_check(password, input_password):
    while input_password != password:
        print("Sorry, that's incorrect.")
        input_password = getpass()
    else:
        return

def save_password():
    # get program name
    jsondata = {}
    print("What program is this password for?")
    program = input()
    while program == "":
        print("Please enter a program name")
        print_lines()
        program = input()
    print("Please enter the password that you would like saved")
    print_lines()
    password = getpass()
    while password == "":
        print("Please enter the password that you would like saved")
        print_lines()
        password = {"Password" : getpass()}
    saved = SaveData(program, password)
    print("Password saved for " + program + "!")
    new_pw_to_file(saved, jsondata)

def get_password():
    print('Please enter the name for the program that you are trying to get')
    print_lines()
    program_name = input()
    password_array = retrieve_pw(program_name)
    if password_array:
        print("Your " + program_name + "password is " + password_array)

try:
    with open(f'app-user.json', 'r', encoding='utf-8') as f:
        app_user = json.load(f, object_hook=SimpleNamespace)
    username = app_user.username
    password = app_user.password
    print('Welcome back ' + username + '!')
    print("Please enter your password")
    print_lines()
    input_password = getpass()
    password_check(password, input_password)
    print("success")
    Condition = True
    while(Condition):
        prompt()
        prompt_answer = input()
        if prompt_answer == "":
            print('please input 1, 2, 3, or 4')
            print_lines()
            input("please press enter")
            Condition = True
        else:
            prompt_answer = int(prompt_answer)

        if prompt_answer == 1:
            save_password()
        elif prompt_answer == 2:
            get_password()
        elif prompt_answer == 3:
            print("answered 3")
        elif prompt_answer == 4:
            Condition = False
    

except:
    
    first_time()
    raise TypeError
