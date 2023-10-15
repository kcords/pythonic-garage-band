class Band:
    pass

class Musician:
    def __init__(self, name):
        self.name = name
        self._instrument = None
        self._role = "Musician"

    def __str__(self):
        return f"My name is {self.name} and I play {self._instrument}"

    def __repr__(self):
        return f"{self._role} instance. Name = {self.name}"


class Guitarist(Musician):
    def __init__(self, name):
        self.name = name
        self._instrument = "guitar"
        self._role = "Guitarist"


class Drummer(Musician):
    def __init__(self, name):
        self.name = name
        self._instrument = "drums"
        self._role = "Drummer"


class Bassist(Musician):
    def __init__(self, name):
        self.name = name
        self._instrument = "bass"
        self._role = "Bassist"