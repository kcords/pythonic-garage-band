class Band:
    pass

class Musician:
    def __init__(self, name):
        self.name = name

class Guitarist(Musician):
    def __str__(self):
        return f"My name is {self.name} and I play guitar"