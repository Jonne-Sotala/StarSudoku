
class User:
    def __init__(self, username, id=None):
        self.id = id
        self.username = username

    def __repr__(self):
        return self.username
