class Person:
    def __init__(self):
        self.person = {
                "fname": "",
                "minit": "",
                "lname": "",
                "home_phone": "",
                "mobile_phone": "",
                "license_ref": [],
                "episode_ref": [],
                }
        self.keys = list(self.person.keys())
        self.values = list(self.person.values())
        self.num = len(self.keys)

    def get_num(self):
        return self.num

    def get_value(self, x):
        return self.values[x]

    def get_key(self, x):
        return self.keys[x]

    def give_value(self, key_num, value):
        self.person.update({self.keys[key_num]: value})

    def get_person(self):
        return self.person
