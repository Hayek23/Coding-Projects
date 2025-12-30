import json

program = '1'
password = {"password": "grrrs"}
jsondata = {}
# jsondata[program] = password


class SaveData:
    def __init__(self, program, password):
        self.program = program
        self.password = password

    def to_dict(self):
        return self.__dict__

saved = SaveData(program, password)



def encode_saved(obj):
    if isinstance(obj, jsondata):
        return obj.to_dict()

# print(jsondata)

def save(program, jsondata):
    jsondata[saved.program] = saved.password
    info = jsondata
    try:
        with open(f'test.json', 'r') as f:
            data = json.load(f)
            if not isinstance(data, list):
                data = []
                print(data)
    except FileNotFoundError:
        data = []
    except json.JSONDecodeError:
        data = []
    print('jsondata' + str(jsondata))
    new_data_dict = jsondata

    data.extend(new_data_dict)
    print(data)

    with open('test.ndjson', 'w') as f:
        f.write(json.dumps(data, indent = 4) + "\n")

save(program, jsondata)



