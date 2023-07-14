
class User:

    def __init__(self, name):
        self.name = name
        self.logged_in = False

    def login(self):
        self.logged_in = True
        print(f"{self.name} is logged in.")

    def logout(self):
        self.logged_in = False
        print(f"{self.name} is logged out.")

    def __repr__(self):
        return f"User({self.name})"
