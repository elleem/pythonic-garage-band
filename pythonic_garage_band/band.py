
class Band:
    instances = []
    def __init__(self,name,members):
        self.name = name
        self.members = members
        Band.instances.append(self)

    def __str__(self):
        return f"Rock band {self.name}"

    def __repr__(self):
        return f'Band instance. Name = {self.name}'

    def play_solos(self):
        return [member.play_solo() for member in self.members]

    @classmethod
    def to_list(cls):
        return cls.instances
class  Musician:
    def __init__(self, name, type, instrument, solo):
        self.name = name
        self.type = type
        self.instrument = instrument
        self.solo = solo

    def __str__(self):
        return f"My name is {self.name} and I play {self.instrument}"

    def __repr__(self):
        return f'Musician instance. Name = {self.name}'


    def get_instrument(self):
        return f"{self.instrument}"

    def play_solo(self):
        return self.solo
class Guitarist(Musician):
    def __init__(self, name):
        super().__init__(name, 'Guitarist', 'guitar', 'face melting guitar solo')

    def __repr__(self):
        # return a string with how to reproduce the object
        return f'Guitarist instance. Name = {self.name}'

class Bassist(Musician):
    def __init__(self, name):
        super().__init__(name, 'Bassist', 'bass', 'bom bom buh bom')

    def __repr__(self):
        # return a string with how to reproduce the object
        return f'Bassist instance. Name = {self.name}'

class Drummer(Musician):
    def __init__(self, name):
        super().__init__(name, 'Drummer', 'drums', 'rattle boom crash')

    def __repr__(self):
        # return a string with how to reproduce the object
        return f'Drummer instance. Name = {self.name}'