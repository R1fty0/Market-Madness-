import json


class User:
    def __init__(self, name, balance, password) -> None:
        self.name = name
        self.balance = balance
        self.password = password

    def to_json(self):
        """ Converts the User object to a JSON string. """
        user_dict = {
            "name": self.name,
            "balance": self.balance,
            "password": self.password
        }
        return json.dumps(user_dict)

    @classmethod
    def from_json(cls, json_str):
        """ Creates a User object from a JSON string. """
        user_dict = json.loads(json_str)
        name = user_dict.get("name")
        balance = user_dict.get("balance")
        password = user_dict.get("password")
        return cls(name, balance, password)


