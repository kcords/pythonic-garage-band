class Band:
    def __init__(self, name, members):
        self.name = name
        self.members = members

    def play_solos(self):
        return [member.play_solo() for member in self.members]


class Musician:
    def __init__(self, name):
        self.name = name
        self._instrument = None
        self._role = "Musician"

    def __str__(self):
        return f"My name is {self.name} and I play {self._instrument}"

    def __repr__(self):
        return f"{self._role} instance. Name = {self.name}"

    def get_instrument(self):
        return self._instrument


class Guitarist(Musician):
    def __init__(self, name):
        self.name = name
        self._instrument = "guitar"
        self._role = "Guitarist"

    def play_solo(self):
        return "face melting guitar solo"


class Drummer(Musician):
    def __init__(self, name):
        self.name = name
        self._instrument = "drums"
        self._role = "Drummer"

    def play_solo(self):
        return "rattle boom crash"


class Bassist(Musician):
    def __init__(self, name):
        self.name = name
        self._instrument = "bass"
        self._role = "Bassist"

    def play_solo(self):
        return "bom bom buh bom"