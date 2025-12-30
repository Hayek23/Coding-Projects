import pickle
class user:
    def __init__(self, name, password):
        self.name = name
        self.password = password
    def get_password(self):
        print(self.password)
u1 = user("Jacob", "password")
with open(f'test.pickle', 'wb') as file:
    pickle.dump(u1, file)

with open(f'test.pickle', 'rb') as file2:
    u1_new = pickle.load(file2)
u1_new.get_password()